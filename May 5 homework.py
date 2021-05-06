day = int(input('Give me a number 0-7 and I\'ll tell you what day it is: '))

if day == 0:
    print('Not a day')
elif day == 1:
    print('Monday')
elif day == 2:
    print ('Tuesday')
elif day == 3:
    print('Wednesday')
elif day == 4:
    print('Thursday')
elif day == 5:
    print('Friday')
elif day == 6:
    print('Saturday')
elif day == 7:
    print('Sunday')

else:
    print('Please give me a valid number')

if day >= 1 and day <= 5:
    print('It\'s time to go to work')
if day == 6 or day == 7:
    print('It\'s the weekend, sleep in')
    