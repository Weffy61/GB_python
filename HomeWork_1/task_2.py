"""
Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

⋀ - and
⋁ - or
¬ - not
not(X or Y or Z) == not X and not Y and not Z
"""

x = int(input('X = '))
y = int(input('Y = '))
z = int(input('Z = '))


side_left = not(x or y or z)
side_right = not x and not y and not z

result = side_left == side_right
print(result)
