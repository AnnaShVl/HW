# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# s = [1,5,9,8]
# total = 0
# for i in range(1,len(s),2):
#     total+=s[i]
# print(total)
s = [1,5,9,8]
s_new = [s[i] for i in range(len(s)) if i%2!=0]
print(sum(s_new))