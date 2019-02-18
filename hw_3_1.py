#!/usr/bin/env python

''' ****************************************
    *  Sum of natural numbers              *
    *  according to ISO 80000-2 standard   *
    ****************************************'''

def main():
    num1 = input('Enter the 1st any number: ')
    num2 = input('\nEnter the 2nd any number: ')

    sum_nat = sum_natural_numbers(num1, num2)
    if num1 < num2:
        print('Sum of natural numbers between {} and {} is {}'.format(num1, num2, sum_nat))
    elif num1 > num2:
        print('Sum of natural numbers between {} and {} is {}'.format(num2, num1, sum_nat))
    input('\nPress Enter to exit')

def sum_natural_numbers(num1, num2):
    num1 = num1.replace(' ', '')

    if (num1.find('-') != -1) or (not num1.replace('.', '', 1).isdigit()):
        num1 = 0
    elif num1.replace('.', '', 1).isdigit() and (num1.find('.') != -1):
        num1 = int(num1[:num1.find('.')]) + 1
    else:
        num1 = int(num1)

    num2 = num2.replace(' ', '')
    if (num2.find('-') != -1) or (not num2.replace('.', '', 1).isdigit()):
        num2 = 0
    elif num2.replace('.', '', 1).isdigit() and (num2.find('.') != -1):
        num2 = int(num2[:num2.find('.')])
    else:
        num2 = int(num2)

    # Check
    if num1 > num2:
        summa = 0
        for x in range(num2, num1 + 1):
            summa += x
        return summa

    elif num1 == num2:
        summa =0
        return summa

    else:
        summa = 0
        for x in range(num1, num2 + 1):
            summa += x
        return summa

main()
