#на входе a = [4, 3, -10, 1, 7, 12], получить на выходе из этого списка  а=[4, -10, 12, 3, 1, 7]
a = [4, 3, -10, 1, 7, 12]
new_a =[]
new_b =[]
for i in range(len(a)):
    if a[i]%2==0:
        new_a.append(a[i])
    else:
        new_b.append(a[i])
print(new_a+new_b)