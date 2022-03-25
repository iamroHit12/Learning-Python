def bubble(list):
    for i in range(len(list)):
        for j in range(len(list)-i-1):
            if list[j] > list[j+1]:
               list[j],list[j+1] = list[j+1],list[j]

    return list

a = [5, 15, 3, 12, 17, 0]
b = [64, 25, 12, 22, 11]

print(bubble(a))
print(bubble(b))