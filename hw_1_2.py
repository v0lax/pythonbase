#!/usr/bin/env python

''' ****************************************
    *   Calculation of binary operations   *
    *                                      *
    ****************************************'''


operand1 = input('''ATTENTION!!!\nThe exponentiation operation\
 for large numbers can take a very long time.
Please use decimal point for real numbers.
Enter the 1st any number: ''')
try:
    operand1 = int(operand1)
except:
    try:
        operand1 = float(operand1)
    except:
        input('The entered is not a number\nPlease try again.')
        exit()


operand2 = input('Enter the 2nd any number: ')
try:
    operand2 = int(operand2)
except:
    try:
        operand2 = float(operand2)
    except:
        input('The entered is not a number\nPlease try again.')
        exit()

# Output the result of all operations on two numbers
print('{} + {} = {}'.format(operand1, operand2, operand1 + operand2))
print('{} - {} = {}'.format(operand1, operand2, operand1 - operand2))
print('{} * {} = {}'.format(operand1, operand2, operand1 * operand2))

try:
    operand1/operand2
except:
    print('Dividing by zero is impossible')
else:
    print('{} / {} = {}'.format(operand1, operand2, operand1 / operand2))
    print('{} // {} = {} (integer division)'.format(operand1, operand2, operand1 // operand2))
    print('{} % {} = {} (remainder of division)'.format(operand1, operand2, operand1 % operand2))

try:
    operand1 ** operand2
except:
    print('{} ** {}. Result too large.'.format(operand1, operand2))
else:
    print('{} ** {} = {}'.format(operand1, operand2, operand1 ** operand2))

input("\nPress 'Enter' to exit")
