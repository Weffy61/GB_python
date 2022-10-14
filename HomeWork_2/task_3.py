"""
Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

Пример:

- Для n = 3: {1: 2.0, 2: 2.25, 3: 2.37
(1 + 1/n)**n
"""

n = int(input("N => "))
my_dict = {i+1: round((1 + 1/k) ** k, 2) for i, k in enumerate(range(1, n+1))}
print(my_dict)

print({i+1: round((1 + 1/k) ** k, 2) for i, k in enumerate(range(1, n+1))})

