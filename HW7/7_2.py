# 3)На вход программы поступает список наименований рек,
# записанных в одну строчку через пробел.
# Необходимо отсортировать этот список в порядке убывания длин названий.
# Результат вывести в одну строчку через пробел.
# Sample Input:
# Лена Енисей Волга Дон
# Sample Output:
# Енисей Волга Лена Дон

list1=['Лена', 'Енисей', 'Волга', 'Дон']
list1.sort(key=len,reverse=True)
print(*list1)

