#User function Template for python3

class Solution:
    def __init__(self):
        self.list0 = []
        self.list1 = []
        self.list2 = []

    def sort012(self,arr,n):
        for el in arr:
            if(el==0):
                self.list0.append(el)
            elif(el==1):
                self.list1.append(el)
            else:
                self.list2.append(el)

        arr = self.list0
        arr.extend(self.list1)
        arr.extend(self.list2)
        
        return arr


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        res = ob.sort012(arr,n)
        for i in res:
            print(i, end=' ')
        print()

# } Driver Code Ends