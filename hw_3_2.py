#!/usr/bin/env python

''' ****************************************
    *  Fibonacci numbers                   *
    *                                      *
    ****************************************'''

def main():
    num = input('''ATTENTION !!!\nCalculating an element of a Fibonacci series
with a large sequence number may take a long time.
Enter the sequence number of the Fibonacci number: ''')
    fibo_num = get_fibonachi(num)
    print('\nThe element [{}] of the Fibonacci number series = {}'.format(num, fibo_num))
    input('\nPress Enter to exit')
    exit()

def get_fibonachi(num):
    err_msg_invalid = 'Invalid data or negative number'
    num = num.replace(' ', '')

    if not num.isdigit():
        input(err_msg_invalid)
        exit()

    num = int(num)

    # Exception for the 1st sequence number
    if num == 1:
        current = 1
        return current

    # Initial initialization
    x1 = 0
    x2 = 1

    _ = 2

    while _ <= num:
        current = x1 + x2
        # reassign values
        x1 = x2
        x2 = current
        _ += 1

    return current

main()