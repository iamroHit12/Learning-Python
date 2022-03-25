def search(arr,n,key):

    for i in range(n):
        if(arr[i] == key):
            return i
    return -1

arr = [2, 3, 4, 10, 40]
key = 10
n = len(arr)

res = search(arr,n,key)

if res == -1:
    print("Not found")
else :
    print("at index",res)