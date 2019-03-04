#!/usr/bin/env python

''' ********************************************
    *  Parser of numbers from the text string  *
    *  (with test function)                    *
    ********************************************'''

def main():

    test_function('kj5p67lljkjkj8')
    test_function('a0s1d2f3g4h5j6kl')
    test_function('2f3g4h5j6kl')
    test_function('2f3g 4h5j6kl')
    test_function('2f8g4h5j6kl')
    test_function('2f3g 4h9j6kl')
    test_function('2f8g 4h5j6kl')

def test_function(text):
    result = get_digits_from_text(text)
    print("'{}' => {}".format(text,result))

def get_digits_from_text(string):
    '''get_digits_from_text(<Text string>)\n\n\
Returns: numbers in case they in ascending order in text string'''

    class ValueError(Exception):
        def __init__(self):
            ValueError.text = 'Ошибка: Недопустимое значение в тексте - пробел.'
    
    class IndexError(Exception):
        def __init__(self):
            IndexError.text = 'Ошибка: Нарушена последовательность цифр.'
            
    
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    
    n1 = None
    n = None
    
    for char_1st in string:
        try:
            if char_1st == ' ':
                raise ValueError
        except ValueError:
            #print("'{}' => {}".format(string, ValueError.text))
            return ValueError.text
            #exit()
        if char_1st in numbers:
            n1 = int(char_1st)
            result = char_1st
            break
    
    for character in string[string.find(char_1st) + 1:]:
        try:
            if character == ' ':
                raise ValueError
        except ValueError:
            return ValueError.text
        if character in numbers:
            n = int(character)
            try:
                if n - n1 == 1:
                    result += character
                    n1 = n
                else:
                    raise IndexError
            except IndexError:
                return IndexError.text
    
    return result


if __name__ == '__main__':
    main()
