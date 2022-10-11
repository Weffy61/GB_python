import random


def randomize(list_num):
    counter = random.randint(1, 5)
    while counter > 0:
        for i in range(len(list_num)):
            for el in range(1, len(list_num)):
                temp = list_num[i]
                list_num[i] = list_num[el]
                list_num[el] = temp
            counter -= 1
    return list_num


number_list = [random.randint(5, 10) for i in range(random.randint(10, 30))]
print(number_list)

print(randomize(number_list))

