list = [1, 2, 3, 4]
list1 = ["python", "thunder"]

n_list = list + list1
print(n_list)

list.extend(list1)
print(list)

for i in list1:
    list.append(i)
print(list)

