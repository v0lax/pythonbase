#!/usr/bin/env python

''' ****************************************
    *  Sum of natural numbers              *
    *  according to ISO 80000-2 standard   *
    ****************************************'''

err_msg_invalid = 'Invalid data or negative number'

num1 = input('Enter 1st number greater than or equal to 0: ')
num1 = num1.replace(' ', '')

if (num1.find('-') != -1) or (not num1.replace('.', '', 1).isdigit()):
    input(err_msg_invalid)
    exit()
elif num1.replace('.', '', 1).isdigit() and (num1.find('.') != -1):
    num1 = int(num1[:num1.find('.')]) + 1
else:
    num1 = int(num1)

num2 = input('\nEnter 2nd number greater than or equal to 0: ')
num2 = num2.replace(' ', '')

if (num2.find('-') != -1) or (not num2.replace('.', '', 1).isdigit()):
    input(err_msg_invalid)
    exit()
elif num2.replace('.', '', 1).isdigit() and (num2.find('.') != -1):
    num2 = int(num2[:num2.find('.')])
else:
    num2 = int(num2)

# Check
if num1 >= num2:
    input('\nThe 2nd number must be greater than the 1st.')
    exit()

# "for"
summa = 0
for x in range(num1, num2 + 1):
    summa += x

print('\n\nThe sum of natural numbers from {} to {} is {} (using "for")'.format(num1, num2, summa))

# "while"
summa = 0
x = num1
while x <= num2:
    summa += x
    x += 1

print('\n\nThe sum of natural numbers from {} to {} is {} (using "while")'.format(num1, num2, summa))

input('\nPress Enter to exit')
