import math
n = int(input("enter the number "))

def order(x):
    i = 0
    while(x != 0):
        i = i + 1
        x = x // 10

    return i

def arm(x):
    nofDigit = order(x)

    originalNo = x;
    sum = 0
    while (x!=0):
        n = x % 10
        sum = sum + math.pow(n,nofDigit)
        x = x//10

    if (originalNo == sum):
        print("armstrong")
    else:
        print("not armstrong")

arm(n)