try:
    list1=[]
    list2=[]
    test = int(input())
    
    for i in range(test):
        list1 = list(map(int,input().split()))
        list2 = list(map(int,input().split()))
        
        sum1 = sum(list1)
        sum2 = sum(list2)
        
        if(sum1>sum2):
            print("DRAGON")
        elif(sum1<sum2):
            print("SLOTH")
        else:
            for j in range(len(list1)):
                if(list1[j]>list2[j]):
                    s = "DRAGON"
                    break
                elif(list1[j]<list2[j]):
                    s = "SLOTH"
                    break
                else:
                    s = "TIE"
            print(s)
        
except:
    pass