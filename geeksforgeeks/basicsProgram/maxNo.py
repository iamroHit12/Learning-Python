a = int(input("1st no"))
b = int(input("2nd no"))

def maximum(x,y):
    if x>y:
        return x
    else:
        return y

print(maximum(a,b))