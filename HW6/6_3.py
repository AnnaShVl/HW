# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# n=int(input())
# mult=1
# for i in range(1,n+1):
#     mult*=i
#     print(mult)

print(list(i*(i+1) for i in range(1,int(input())+1)))