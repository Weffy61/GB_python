"""
Напишите программу, в которой пользователь будет задавать две строки, а программа - определять
количество вхождений одной строки в другой.
Пример:
"hello or world", "or" -> 2
"""
#
# phrase_1 = str(input('Input string_1 => '))
# phrase_2 = str(input('Input string_2 => '))
#
# counter = 0
#
# for i in range(0, len(phrase_1), len(phrase_2)):
#     if phrase_1[i:i+len(phrase_2)] == phrase_2:
#         counter += 1
#
#
# print(counter)


str = input("Введите строку: ")
substr = input("Введите подстроку: ")

found_cnt = 0

for i in range(len(str) - len(substr) + 1):
    if str[i: i + len(substr)] == substr:
        found_cnt += 1

print(found_cnt)