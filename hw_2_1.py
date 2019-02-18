#!/usr/bin/env python

''' ****************************************
    *  Sum of natural numbers              *
    *  according to ISO 80000-2 standard   *
    ****************************************'''

#err_msg_invalid = 'Invalid data or negative number'

num1 = input('Enter 1st number greater than or equal to 0: ')
num1 = num1.replace(' ', '')

if (num1.find('-') != -1) or (not num1.replace('.', '', 1).isdigit()):
    num1 = 0
#    input(err_msg_invalid)
#    exit()
elif num1.replace('.', '', 1).isdigit() and (num1.find('.') != -1):
    num1 = int(num1[:num1.find('.')]) + 1
else:
    num1 = int(num1)

num2 = input('\nEnter 2nd number greater than or equal to 0: ')
num2 = num2.replace(' ', '')

if (num2.find('-') != -1) or (not num2.replace('.', '', 1).isdigit()):
    num2 = 0
#    input(err_msg_invalid)
#    exit()
elif num2.replace('.', '', 1).isdigit() and (num2.find('.') != -1):
    num2 = int(num2[:num2.find('.')])
else:
    num2 = int(num2)

# Check
if num1 > num2:
    summa = 0
    for x in range(num2, num1 + 1):
        summa += x
    print('\n\nThe sum of natural numbers from {} to {} is {} (using "for")'.format(num2, num1, summa))

    summa = 0
    x = num2
    while x <= num1:
        summa += x
        x += 1
    print('\n\nThe sum of natural numbers from {} to {} is {} (using "while")'.format(num2, num1, summa))

elif num1 == num2:
    summa =0
    print('\n\nThe sum of natural numbers from {} to {} is {}'.format(num1, num2, summa))

else:
    summa = 0
    for x in range(num1, num2 + 1):
        summa += x
    print('\n\nThe sum of natural numbers from {} to {} is {} (using "for")'.format(num2, num1, summa))

    summa = 0
    x = num1
    while x <= num2:
        summa += x
        x += 1
    print('\n\nThe sum of natural numbers from {} to {} is {} (using "while")'.format(num1, num2, summa))

input('\nPress Enter to exit')
