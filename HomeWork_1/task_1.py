"""
Напишите программу, которая принимает на вход цифру, обозначающую день недели, и
проверяет, является ли этот день выходным.
"""

number = int(input("Enter a number from 1 to 7 representing the corresponding day of the week => "))
if 6 > number > 0:
    print("Working day")
elif 5 < number < 8:
    print("Day off")
else:
    print("Nonexistent day of the week")


