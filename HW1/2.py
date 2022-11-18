1.	# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.


x_value = int(input('Введите значение числа X: '))
y_value = int(input('Введите значение числа Y: '))
z_value = int(input('Введите значение числа Z: '))

if not (x_value or y_value or z_value) == (not (x_value) and not (y_value) and not (z_value)):
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z явлется верным')
else:
    print('Утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z явлется неверным')