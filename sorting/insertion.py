def insertion(list):
    for i in range(1,len(list)):
        current = list[i]
        j = i-1

        while j>=0 and current<list[j]:
            list[j+1] = list[j]
            j = j-1
        list[j+1] = current

    return list

a = [5, 15, 3, 12, 17, 0]
b = [64, 25, 12, 22, 11]

print(insertion(a))
print(insertion(b))