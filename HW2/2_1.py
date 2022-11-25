# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

n = float(input())
n= str(n)
total = 0
n = int(n.replace('.',''))
while n != 0:
    total = total + n%10
    n=n//10
print(total)