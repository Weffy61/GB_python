"""
Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных
координат точек в этой четверти (x и y).
"""

quarter = int(input('Enter a quarter(1-4) => '))

if quarter == 1:
    print('x and y > 0')
elif quarter == 2:
    print('x < 0 < y')
elif quarter == 3:
    print('x and y < 0')
elif quarter == 4:
    print('x > 0 > y')
else:
    print('You had entered incorrect data')
