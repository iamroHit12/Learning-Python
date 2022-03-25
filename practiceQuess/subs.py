t = "ahbgdc"
s = "axc"

lt = len(t)
ls = len(s)
list1 = []

for el in s:
    if el in t:
        for i in range(lt):
            if(el == t[i]):
                index = i
                list1.append(i)

print(list1)       

if(len(list1)<ls):
    print("No")
elif(list1 != sorted(list1)):
    print("No")
else:
    print("Yes")