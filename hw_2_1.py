#!/usr/bin/env python

''' ****************************************
    *  Sum of natural numbers              *
    *  according to ISO 80000-2 standard   *
    ****************************************'''

#err_msg_invalid = 'Invalid data or negative number'

num1 = input('Enter the 1st any number: ')
num1 = num1.replace(' ', '')

if (num1.find('-') != -1) or (not num1.replace('.', '', 1).isdigit()):
    num1 = 0
else:
    num1 = float(num1)
    

num2 = input('\nEnter the 2nd any number: ')
num2 = num2.replace(' ', '')

if (num2.find('-') != -1) or (not num2.replace('.', '', 1).isdigit()):
    num2 = 0
else:
    num2 = float(num2)


if int(num1) == int(num2):
    summa =0
    print('\n\nThe sum of natural numbers from {} to {} is {}'.format(int(num1), int(num2), summa))
    input('\nPress Enter to exit')
    exit()
elif num1 > num2:
    num1, num2 = num2, num1

if num1 > int(num1):
   num1 = int(num1) + 1

num1 = int(num1)
num2 = int(num2)

summa = 0
for x in range(num1, num2 + 1):
    summa += x
print('\n\nThe sum of natural numbers from {} to {} is {} (using "for")'.format(num1, num2, summa))

summa = 0
x = num1
while x <= num2:
    summa += x
    x += 1 
print('\n\nThe sum of natural numbers from {} to {} is {} (using "while")'.format(num1, num2, summa))

input('\nPress Enter to exit')
