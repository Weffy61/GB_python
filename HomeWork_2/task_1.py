"""
Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
Пример:

- 6782 -> 23
- 0,56 -> 11
"""

num = str(input('Number => '))
sum = 0

for i in str(num):
    if i.isdigit():
        sum += int(i)

print(round(sum))
