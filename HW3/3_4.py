# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
n = int(input('введите число: '))
s = ''
while n>0:
    s=str(n%2)+s
    n= n//2
print(s)
