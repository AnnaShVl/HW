# Реализуйте алгоритм перемешивания списка.
#s = [1,2,3,4,5,6,8,9,]
#print(*s)
#from  random import shuffle
#shuffle(s)
#print(s)

s = [1,2,3,4,5,6,8,9]
import random
list_length = len(s)
for i in range(list_length):
        index_new = random.randint(0, list_length - 1)  # Получение случайного индекса
        temp = s[i] #замена
        s[i] = s[index_new]
        s[index_new] = temp
print(s)
