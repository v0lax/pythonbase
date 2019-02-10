#!/usr/bin/env python

''' **************************************************************
    *     Calculation of the number of days, months and years    *
    *     from the date of birth to the specified date           *
    ************************************************************** '''

CURRENT_YEAR = 2019
START_DAY = 31             # Course start day
START_MONTH = 1            # Course start month

# Request the user name and surname. Greetings to him.
user_name = input('Please enter your name: ')
user_surname = input('Please enter your surname: ')
print ('Hello ' + user_name + ' ' + user_surname + '!')

####################################
# Request the birthday information
####################################

day_of_birth = input('What day were you born?\n')

# Checking entered data
try:
   day_of_birth = int(day_of_birth)
except:
   input('This is not an integer !!!\nPlease try again.')
   exit()
else:
   if (day_of_birth < 1) or (day_of_birth > 31):
      input('Day should be in the range of 1 to 31\nPlease try again.')
      exit()

month_of_birth = input('What month were you born? (Please enter the month number,\
for example, "8" for August)\n')

# Checking entered data
try:
   month_of_birth = int(month_of_birth)
except:
   input('This is not an integer !!!\nPlease try again.')
   exit()
else:
   if (month_of_birth < 1) or (month_of_birth > 12):
      input('Month should be in the range of 1 to 12\nPlease try again.')
      exit()

year_of_birth = input('What year were you born?\n')

# Checking entered data
try:
   year_of_birth = int(year_of_birth)
except:
   input('This is not an integer !!!\nPlease try again.')
   exit()
else:
   if (year_of_birth > CURRENT_YEAR):
      input("Really? Look, you're from the future\nUnable to calculate future date")
      exit()

######################################
# Request the current date
######################################
current_day = input('Enter current day of the month\n')

# Checking entered data
try:
   current_day = int(current_day)
except:
   input('This is not an integer !!!\nPlease try again.')
   exit()
else:
   if (current_day < 1) or (current_day > 31):
      input('Day should be in the range of 1 to 31\nPlease try again.')
      exit()

current_month = input('Enter current month number\n')

# Checking entered data
try:
   current_month = int(current_month)
except:
   input('This is not an integer !!!\nPlease try again.')
   exit()
else:
   if (current_month < 1) or (current_month > 12):
      input('Month should be in the range of 1 to 12\nPlease try again.')
      exit()

######################################
# Calculations
######################################

# QTY of full years

full_years = CURRENT_YEAR - year_of_birth
if current_month < month_of_birth:
   full_years -= 1
elif current_month == month_of_birth and current_day < day_of_birth:
   full_years -= 1

# QTY of month
if (current_month * 100 + current_day) >= (month_of_birth * 100 + day_of_birth):
   months = ((current_month * 100 + current_day) - (month_of_birth * 100 + day_of_birth)) // 100
else:
   months = (1200 - (month_of_birth * 100 + day_of_birth) + (current_month * 100 + current_day)) // 100

# QTY of month for START_DAY.START_MONTH
if (START_MONTH * 100 + START_DAY) >= (month_of_birth * 100 + day_of_birth):
   months2 = ((START_MONTH * 100 + START_DAY) - (month_of_birth * 100 + day_of_birth)) // 100
else:
   months2 = (1200 - (month_of_birth * 100 + day_of_birth) + (START_MONTH * 100 + START_DAY)) // 100

# QTY of days
days = abs(START_DAY - day_of_birth)
   

print('On {}.{}.{} you lived {} years and {} month(s)'.format(current_day, current_month, CURRENT_YEAR, full_years, months))
print('On {}.{}.{} you lived {} years, {} month(s) and {} day(s)'.format(START_DAY, START_MONTH, CURRENT_YEAR, full_years, months, days))

input("\nPress 'Enter' to exit")
