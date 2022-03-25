def selection(list):
    for i in range(len(list)):
        min_index = i

        for j in range(i+1,len(list)):
            if list[j] < list[min_index]:
                min_index = j

        list[i],list[min_index] = list[min_index],list[i]

    return list

a = [5, 15, 3, 12, 17, 0]
b = [64, 25, 12, 22, 11]

print(selection(a))
print(selection(b))