class Solution:
    def isSubsequence(self, s, t):
        self.s = s
        self.t = t
        count = 0
        list1 = []

        for el in range(len(s)):
            for i in range(count,len(self.t)):
                if(s[el] == t[i]):
                    list1.append(i)
                    count = i      
        set1 = set(list1)
        print(list1)
        print(set1)
        if(len(list1)<len(self.s)):
            return False
        elif(list1 != sorted(list1)):
            return False
        elif(len(list1)!= len(set1)):
            return False
        else:
            return True
            
sol1 = Solution()
s=input()
t=input()
print(sol1.isSubsequence(s,t))