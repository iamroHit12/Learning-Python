def main():
    List = []

    n = int(input("enter no of element "))
    for i in range(n):
        el = int(input("enter value "))
        List.append(el)

    for i in range(3):
        val = List[n-1]
        List.pop(n-1)
        List.insert(0,val)
    
    print(List)

main()