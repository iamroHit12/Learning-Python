n = int(input("enter no of element "))


def array(x):
    arr = []
    for i in range(0,x):
        ele = int(input())
        arr.append(ele)

    print(sum(arr))

array(n)
