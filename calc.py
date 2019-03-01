#!/usr/bin/env python

''' ********************************
    *    Simplest calculator       *
    *                              *
    ********************************'''

__version__ = '0.0.0.1'

def main():
    print('''This is the simplest calculator.
Valid operations:
    addition                    "+"
    subtraction                 "-"
    multiplication              "*"
    division                    "/"
    integer division            "//"
    remainder of the division   "%"
    exponentiation              "**"

Enter "Q" to exit''')

    arg1, arg2 = 0, 0
    result = None
    continue_calculation_flag = False

    while True:
        
        if continue_calculation_flag == False:
            arg1 = input('Enter 1st operand >> ')
            exit_check(arg1)
            if validate_arguments(arg1) == None:
                continue
            else:
                arg1 = validate_arguments(arg1)

        operation = input('Enter operation ("C" to reset the result)>> ')
        if exit_check(operation) == 'c':
            arg1 = 0
            continue_calculation_flag = False
            continue
        if validate_operations(operation) == False:
            continue
        else:
            operation = validate_operations(operation)

        arg2 = input('Enter 2nd operand >> ')
        exit_check(arg2)
        if validate_arguments(arg2) == None:
            continue
        else:
            arg2 = validate_arguments(arg2)

        result = calc(arg1, arg2, operation)
        if result is not None:
            continue_calculation_flag = True
            print('{} {} {} = {}'.format(arg1, operation, arg2, result))
            arg1 = result
        else:
            print()


def calc(arg1, arg2, operation):

    op = operation.strip()
    if op == '+':
        result = arg1 + arg2
    elif op == '-':
        result = arg1 - arg2
    elif op == '*':
        result = arg1 * arg2
    elif op == '/':
        try:
            result = arg1 / arg2
        except (ZeroDivisionError, Exception) as err:
            print('Error:', err)
            result = None
    elif op == '//':
        try:
            result = arg1 // arg2
        except (ZeroDivisionError, Exception) as err:
            print('Error:', err)
            result = None
    elif op == '%':
        try:
            result = arg1 % arg2
        except (ZeroDivisionError, Exception) as err:
            print('Error:', err)
            result = None
    elif op == '**':
        try:
            result = arg1 ** arg2
        except (OverflowError, Exception) as err:
            print('Error:', err)
            result = None

    return result


def validate_arguments(param):
    try:
        param = float(param.strip().replace(',','.'))
    except ValueError as err:
        print('Error:', err, '\n', 'Please try again', '\n')
        return None
    else:
        return param

def validate_operations(param):
    oper = ['+','-','*','/','//','%','**']
    if oper.count(param) != 1:
        print('Error: operation {} unable to perform'.format(param),'\n', 'Please try again', '\n')
        return False
    else:
        return param


def exit_check(param):
    if param.strip().lower() == 'q':
        input('\nProgram completed')
        exit()
    elif param.strip().lower() == 'c':
        return 'c'


main()