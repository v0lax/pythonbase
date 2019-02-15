#!/usr/bin/env python

''' ****************************************
    *  Fibonacci numbers                   *
    *                                      *
    ****************************************'''

err_msg_invalid = 'Invalid data or negative number'

num = input('''ATTENTION !!!\nCalculating an element of a Fibonacci series
with a large sequence number may take a long time.
Enter the sequence number of the Fibonacci number: ''')
num = num.replace(' ', '')

if not num.isdigit():
    input(err_msg_invalid)
    exit()

num = int(num)

# Exception for the 1st sequence number
if num == 1:
    current = 1
    print('The element [{}] of the Fibonacci number series = {}'.format(num, current))
    input('\nPress Enter to exit')
    exit()

# Initial initialization
x1 = 0
x2 = 1

# "for"
for _ in range(2, num + 1):
    current = x1 + x2
    # reassign values
    x1 = x2
    x2 = current

print('\nThe element [{}] of the Fibonacci number series = {} (using "for")'.format(num, current))

# "while"
# Re-initialization
x1 = 0
x2 = 1
_ = 2

while _ <= num:
    current = x1 + x2
    # reassign values
    x1 = x2
    x2 = current
    _ += 1

print('\nThe element [{}] of the Fibonacci number series = {} (using "while")'.format(num, current))

input('\nPress Enter to exit')
