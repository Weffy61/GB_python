"""
Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и
выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
"""

x = int(input('X = '))
y = int(input('Y = '))


if x > 0 and y > 0:
    print('1st quarter')
elif x < 0 < y:
    print('2nd quarter')
elif x < 0 and y < 0:
    print('3rd quarter')
elif x > 0 > y:
    print('4th quarter')

else:
    print('You had entered data that does not match the condition')
