print('Enter the current date by month, day, and year\n' 'Month: ')
currentMonth = int(input())
print('Day:')
currentDay = int(input())
print('Year:')
currentYear = int(input())
print('Enter your birthday by month, day, and year\n' 'Month: ')
birthdayMonth = int(input())
print('Day:')
birthdayDay = int(input())
print('Year:')
birthdayYear = int(input())

userAge = currentYear - birthdayYear - ((currentMonth, currentDay) < (birthdayMonth, birthdayDay))
print('You are', userAge, 'years old.')
if (currentMonth == birthdayMonth) and (currentDay == birthdayDay):
    print('Happy Birthday!')