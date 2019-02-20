#!/usr/bin/env python

''' *****************************************************
    *  Conversion of numbers                            *
    *  to binary, octal and hexadecimal number systems  *
    *****************************************************'''

def main():
    try:
        dec = int(input('Enter integer number: '))
    except:
        input('This is not an integer !!!\nPlease try again.')
        exit()
    calc_bin = my_bin(dec)
    calc_oct = my_oct(dec)
    calc_hex = my_hex(dec)
    print('dec: ',dec)
    print('bin: ',calc_bin)
    print('oct: ',calc_oct)
    print('hex: ',calc_hex)
    input('\nPress Enter to exit')

def my_bin(dec):

    if dec < 0:
       dec = abs(dec)
       sign = '-'
    else:
       sign = ''

    result = ''
    while dec // 2 >= 1:
        bin = dec % 2
        dec //= 2
        result = str(bin) + result

    result = sign + str(dec) + result
    return result

def my_oct(dec):

    if dec < 0:
       dec = abs(dec)
       sign = '-'
    else:
       sign = ''

    result = ''
    while dec // 8 >= 1:
        oct_ = dec % 8
        dec //= 8
        result = str(oct_) + result

    result = sign + str(dec) + result
    return result

def my_hex(dec):

    if dec < 0:
       dec = abs(dec)
       sign = '-'
    else:
       sign = ''
    result = ''

    while dec // 16 >= 1:
        hex_ = dec % 16
        if hex_ == 10:
            hex_ = 'A'
        elif hex_ == 11:
            hex_ = 'B'
        elif hex_ == 12:
            hex_ = 'C'
        elif hex_ == 13:
            hex_ = 'D'
        elif hex_ == 14:
            hex_ = 'E'
        elif hex_ == 15:
            hex_ = 'F'
    
        dec //= 16
        result = str(hex_) + result

    if dec == 10:
        dec = 'A'
    elif dec == 11:
        dec = 'B'
    elif dec == 12:
        dec = 'C'
    elif dec == 13:
        dec = 'D'
    elif dec == 14:
        dec = 'E'
    elif dec == 15:
        dec = 'F'
    
    result = sign + str(dec) + result
    return result
    
main()
