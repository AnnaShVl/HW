# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

with open('text_5_1.txt','w', encoding='utf-8') as file:
    file.write(input('Введите текст: '))
with open('text_5_1.txt','r', encoding='utf-8') as file:
    my_text = file.readline()
    first_text = my_text.split()
#print(my_text)

del_text = 'абв'

result = ' '.join(filter(lambda x: del_text not in x, first_text))
with open('text_res_5_1.txt','w', encoding='UTF-8') as file:
    file.write(f'{result}')
print(result)