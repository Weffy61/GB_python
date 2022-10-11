"""
Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение
элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
"""
import random


def generate_num():
    n = random.randint(5, 10)
    num = []
    for i in range(-n, n+1):
        num.append(i)
    print(num)
    return num


def create_index():
    ind = []
    with open('task_4/num.txt', 'r') as file:
        for i in file:
            i = i.rstrip('\n')
            if i.isdigit():
                ind.append(int(i))
    return ind


def get_result(index_list, numbers_list):
    result = 1
    try:
        for i in index_list:
            result *= numbers_list[i]
            print(f'{numbers_list[i]}',  end=' ')
    except Exception as _ex:
        print(_ex)
        result = 0
    finally:
        print(f'\nResult is {result}')


numbers = generate_num()
index = create_index()
get_result(index, numbers)





