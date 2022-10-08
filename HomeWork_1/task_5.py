"""
Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
"""
import math

x_1 = float(input('X coordinate for 1st point => '))
y_1 = float(input('Y coordinate for 1st point => '))
x_2 = float(input('X coordinate for 2nd point => '))
y_2 = float(input('Y coordinate for 2nd point => '))

cat_1 = x_2 - x_1
cat_2 = y_2 - y_1

result_1 = round(((cat_1 * cat_1 + cat_2 * cat_2) ** 0.5), 3)

result_2 = round(math.sqrt(cat_1 * cat_1 + cat_2 * cat_2), 3)

print(f'1. The distance between two points is {result_1}')
print(f'2. The distance between two points is {result_2}')
