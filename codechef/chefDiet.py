try:
    test = int(input())

    for i in range(test):
        N, K = [int(x) for x in input().split()]
        num = [int(num) for num in input().split(" ",N-1)]
        
        flag = False
        rem = 0
        for j in range(N):
            if(num[j]>=K):
                flag = True
                rem = num[j] - K
                if (j+1)<=(N-1):
                    num[j+1] = num[j+1] + rem
            else:
                flag = False
                break    
        if(flag):
            print("YES")
        else:
            print("NO",j+1)
except:
    pass