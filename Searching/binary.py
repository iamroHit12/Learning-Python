def binary(list1,key):
    low = 0
    high = len(list1) - 1

    while low <= high:

        mid = low + (high - low) // 2

        if key == list1[mid]:
            return mid
        elif key > list1[mid]:
            low = mid + 1
        else :
            high = mid - 1

list1 = [23, 1, 4, 2, 3]
list1.sort()

key = int(input())

res = binary(list1,key)

if res == None:
    print("not found")
else:
    print("at index",res)