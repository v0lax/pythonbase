#!/usr/bin/env python

''' ****************************************
    *  Calculation of "+"/"*" operations   *
    *                                      *
    ****************************************'''

str1 = input('Enter the 1st integer number: ')
try:
    int(str1)
except:
    input('The entered is not integer number\nPlease try again.')
    exit()

print('Integer = ', int(str1))
print('Real = ', float(str1))
print('Bool = ', bool(str1))
print('String = ' + '"' + str1 + '"')

str2 = input('Enter the 2nd integer number: ')
try:
    int(str2)
except:
    input('The entered is not integer number\nPlease try again.')
    exit()


# New variables to simplify

int1 = int(str1)
real1 = float(str1)
bool1 = bool(str1)

int2 = int(str2)
real2 = float(str2)
bool2 = bool(str2)

print('Integer * Integer =', int1 * int2)
print('Integer * Real =', int1 * real2)
print('Integer * Boolean =', int1 * bool2)
print('Integer * String =', int1 * str2)

print('Real * Integer =', real1 * int2)
print('Real * Real =', real1 * real2)
print('Real * Boolean =', real1 * bool2)
print('Real * String: TypeError')

print('Boolean * Integer =', bool1 * int2)
print('Boolean * Real =', bool1 * real2)
print('Boolean * Boolean =', bool1 * bool2)
print('Boolean * String =', bool1 * str2)

print('String * Integer =', str1 * int2)
print('String * Real: TypeError')
print('String * Boolean =', str1 * bool2)
print('String * String: TypeError')

print('Integer + Integer =', int1 + int2)
print('Integer + Real =', int1 + real2)
print('Integer + Boolean =', int1 + bool2)
print('Integer + String: TypeError')

print('Real + Real =', real1 + real2)
print('Real + Boolean =', real1 + bool2)
print('Real + String: TypeError')

print('Boolean + Boolean =',bool1 + bool2)
print('Boolean + String: TypeError')

print('String + String =', str1 + str2)

input("\nPress 'Enter' to exit")
