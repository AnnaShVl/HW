# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('4_5_1.txt','r') as file:
    poly_1 = file.readline()
    list_of_poly_1 = poly_1.split()

with open('4_5_2.txt','r') as file:
    poly_2 = file.readline()
    list_of_poly_2 = poly_2.split()

poly_1 = poly_1.split(' + ')
poly_2 = poly_2.split(' + ')
print(poly_1,poly_2)

sum_poli_common = []
order_k_common =[]
for i in range(len(poly_1)):
    for j in range(len(poly_2)):
        if (poly_1[i][(poly_1[i].rfind('*'))+1:])== (poly_2[j][(poly_2[j].rfind('*'))+1:]): # степень одночлена
            sum_poli_common.append(int(poly_1[i][:(poly_1[i].find('*'))])+int(poly_2[j][:(poly_2[j].find('*'))]))  # множитель одночлена
            order_k_common.append(poly_1[i][(poly_1[i].rfind('*'))+1:])
#print(sum_poli_common, order_k_common)

sum_poli_dif = []
order_k_dif =[]
if len(poly_1)<len(poly_2):
    poly_1, poly_2=poly_2,poly_1
delta_len=(len(poly_1)-len(poly_2))
for i in range(0,delta_len):
    sum_poli_dif.append(int(poly_1[i][:(poly_1[i].find('*'))]))
    order_k_dif.append(poly_1[i][(poly_1[i].rfind('*')) + 1:])
#print(sum_poli_dif, order_k_dif)

sum_poly=sum_poli_dif+sum_poli_common
order_k=order_k_dif+order_k_common
#print(sum_poly, order_k)

sum_to_write = []
for i in range(len(sum_poly)):
    sum_to_write.append(str(sum_poly[i])+'*x**'+str(order_k[i]))
print(' + '.join(sum_to_write))

with open('4_5_sum.txt', 'w', encoding='utf-8') as file:
    file.write(' + '.join(sum_to_write))