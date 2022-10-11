"""
Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

Пример:

- пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""

result = 1
resilt_lst = []
n = int(input("N => "))

for i in range(1, n+1):
    resilt_lst.append(i * result)
    result *= i

print(result)
print(resilt_lst)
