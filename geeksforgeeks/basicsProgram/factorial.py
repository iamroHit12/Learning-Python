n = int(input("enter the number "))

# iterative function
def fact(a):
    sum = 1
    for x in range(1,n+1):
        sum = sum * x

    return sum

print(fact(n))

# recursive function

def facto(a):
    return 1 if a == 1 or a == 0 else facto(a-1) * a

print(facto(5))