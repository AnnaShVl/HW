# Задайте последовательность чисел.
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
s = list(input())
s_new=[]
for i in range(len(s)):
    if s[i] not in s_new:
        s_new.append(s[i])
print(s_new)
