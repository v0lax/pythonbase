#!/usr/bin/env python

''' ****************************************
    *    Text statistics calculation       *
    *                                      *
    ****************************************'''
__version__ = '0.3'

def main():
#    text = '''1. Этот текст	является материалом для экспериментов.
#2. И этот ТЕКСТ специально подобран для проверки статистики.
#'''
    text = ''
    
    print('Введите текст. Пустая строка - прекращение ввода.\n<--- Текст ---')
   
    while True:
        single_line = input()
        if single_line != '':
           text += single_line + '\n'
        else:
            break
    print('--- Текст --->\n')

    exclude_words = input('''Введите слова, которые нужно исключить из подсчета статистики.
В качестве разделителя используйте пробел или табуляцию)\n''')

    print('--- Текст --->\n')

    words_stat, chars_stat, digits, lines = text_stat(text, exclude_words)

    print ('\nВсего строк = {}\n'.format(lines))
    print ('Всего цифр =  {}\n'.format(digits))

    chars = chars_stat.keys()
    words = words_stat.keys()

    print('<--- Статистика символов ---')
    for x in chars:
        print('{} = {}'.format(repr(x), chars_stat[x]))
    print('--- Статистика символов --->\n')
    input('Нажмите <Enter> для продолжения вывода')

    print('\n<--- Статистика слов ---')
    for x in words:
        print('{} = {}'.format(x, words_stat[x]))
    print('--- Статистика слов --->\n')
    input('Нажмите <Enter> для выхода')
    

def text_stat(text, exclude_words):
    '''text_stat(<Text string to calculate text statistics>, 
          <Text string with words to exclude from statistics>) \n\n\
Returns:
"words_stat": a dictionary of words in which words are keys and values is the quantity of a word
"chars_stat": a dictionary of characters (both printable and non-printable) in which characters
              are keys and values is the quantity of a character
"digits": total number of digits in the text
"lines": total number of lines in text'''

    
    #exclude_words = '1.   2.   Этот   текст   		дЛя  и'

    words_stat = dict((x, text.lower().split().count(x)) for x in text.lower().split())

    exclude_words = tuple(exclude_words.split())

    if len(exclude_words):

        # Select non-printable characters
        non_print_chars = ''
        for x in text:
            if ord(x) in (9, 10, 32):
                non_print_chars += x

        chars_stat = dict((x, non_print_chars.count(x)) for x in sorted(set(non_print_chars)))
        words_stat = {x:_ for x, _ in words_stat.items() if x.lower() not in \
                          tuple(z for z in tuple(j.lower() for j in exclude_words))}

        print_chars = '' 
        for x in words_stat:
            print_chars += str(x)

        # Add filtered characters to the dictionary    
        chars_stat.update((x, print_chars.count(x)) for x in sorted(set(print_chars)))

    else:
        chars_stat = dict((x, text.count(x)) for x in set(text))

    chars = chars_stat.keys()

    digits = 0
    lines = 0
    for x in chars:
        if ord(x) == 10:
            lines = chars_stat[x]
        elif x.isdigit():
            digits += 1

    return words_stat, chars_stat, digits, lines

main()