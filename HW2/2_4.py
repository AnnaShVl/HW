#Задайте список из N элементов, заполненных числами из промежутка [-N, N].
#Найдите произведение элементов на указанных позициях.
#Позиции хранятся в файле file.txt в одной строке одно число.
n = int(input('введите число '))
s = []
import random
for i in range(n):
    s.append(random.randint(-n, n))
print(s)
x=open('file.txt','r', encoding='utf-8')
result_s = [line.strip() for line in x.readlines()]
mult=1
for i in range(len(result_s)):
    mult*=(s[int(result_s[i])])
print(mult)