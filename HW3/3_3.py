# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
s = [1.1, 1.2, 3.1, 5, 10.01]
s1 = []
import math
for i in range(len(s)):
    s1.append(s[i]-math.floor(s[i]))
s1_min = 1
for i in range(len(s1)):
    if s1[i]>0:
        if s1[i]<s1_min:
            s1_min=s1[i]
print(round((max(s1)-s1_min),10))