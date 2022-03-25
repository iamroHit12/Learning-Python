try:
    test = int(input())
    for i in range(test):
        N, P, X, Y = [int(x) for x in input().split()]
        ai = [int(num) for num in input().split(" ",N-1)]
        sum = 0
        for j in range(P):
            if(ai[j] == 0):
                sum = sum + X
            if(ai[j] == 1):
                sum = sum + Y
                
        print(sum)
except:
    pass