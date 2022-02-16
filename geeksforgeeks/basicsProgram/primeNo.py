n = int(input("enter no "))

def primeNo(x):
    if(x==0):
        print("not a prime")
    elif(x>0):
        for i in range(2,x//2 + 1):
            if(x%i==0):
                print("not a prime")
                break
        else:
            print("prime no")
    else:
        print("not a prime")

primeNo(n)