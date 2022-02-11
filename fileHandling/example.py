n = int(input("enter 0 or 1 : "))
if(n == 1):
    f=open("abc.txt","a")
    f.write("more content is waiting...")
    f.close()
    f=open("abc.txt")
    print(f.read())
else:
    print("no file")