"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:

- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37
(1 + 1/n)**n
"""

n = int(input("N => "))
my_lst = []
result = 0

for i in range(1, n+1):
    my_lst.append(round((1 + 1/i) ** i, 2))


for i in my_lst:
    result += i

print(my_lst)
print(round(result, 2))
