#!/usr/bin/env python

''' ****************************************
    *    Text statistics calculation       *
    *                                      *
    ****************************************'''

__version__ = '0.1'

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
    words_stat, chars_stat, digits, lines = text_stat(text)

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

def text_stat(text):
    '''text_stat(<Text string to calculate text statistics>)\n\n\
Returns:
"words_stat": a dictionary of words in which words are keys and values is the quantity of a word
"chars_stat": a dictionary of characters (both printable and non-printable) in which characters
              are keys and values is the quantity of a character
"digits": total number of digits in the text
"lines": total number of lines in text'''

    chars_stat = dict((x, text.count(x)) for x in set(text))
    chars = chars_stat.keys()

    words_stat = dict((x, text.lower().split().count(x)) for x in text.lower().split())

    digits = 0
    lines = 0
    for x in chars:
        if ord(x) == 10:
            lines = chars_stat[x]
        elif x.isdigit():
            digits += 1

    return words_stat, chars_stat, digits, lines

main()
