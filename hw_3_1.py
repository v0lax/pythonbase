#!/usr/bin/env python

''' ****************************************
    *  Sum of natural numbers              *
    *  according to ISO 80000-2 standard   *
    ****************************************'''

def main():
    num1 = input('Enter the 1st any number: ')
    num2 = input('\nEnter the 2nd any number: ')

    sum_nat = sum_natural_numbers(num1, num2)[0]
    x1 = sum_natural_numbers(num1, num2)[1]
    x2 = sum_natural_numbers(num1, num2)[2]

    print('\nSum of natural numbers between {} and {} is {}'.format(x1, x2, sum_nat))
    input('\nPress Enter to exit')

def sum_natural_numbers(num1, num2):
    '''The "sum_natural_numbers" function returns the sum of natural numbers between a range of numbers.'''

    num1 = num1.replace(' ', '')

    if (num1.find('-') != -1) or (not num1.replace('.', '', 1).isdigit()):
        num1 = 0
    else:
        num1 = float(num1)

    num2 = num2.replace(' ', '')

    if (num2.find('-') != -1) or (not num2.replace('.', '', 1).isdigit()):
        num2 = 0
    else:
        num2 = float(num2)

    
    if int(num1) == int(num2):
        summa =0
        return summa, int(num1), int(num2)
    elif num1 > num2:
        num1, num2 = num2, num1
    
    if num1 > int(num1):
       num1 = int(num1) + 1
    
    num1 = int(num1)
    num2 = int(num2)
    
    summa = 0
    for x in range(num1, num2 + 1):
        summa += x
    return summa, num1, num2

main()
