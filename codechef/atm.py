try:
    test = int(input())
    list1 = []
    money = []
    
    for i in range(test):
        N, K = input().split()
        K = int(K)
        money = list(map(int, input().split()))
        
        for j in range(int(N)):
            if money[j] <= K:
                K = K-money[j]
                list1.append(1)
            else:
                list1.append(0)
                
        print(''.join(map(str,list1)))
except:
    pass