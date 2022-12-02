# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  Пример:
#  - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
from random import randint
k = int(input())
koeff=[randint(0,101) for i in range(k)]+[randint(1,101)]
poly='+'.join([f'{(j,"")[j==1]}x**{i}' for i, j in enumerate(koeff) if j][::-1])
print(poly)

with open('file4_4.txt', 'w') as data:
    data.write(poly)