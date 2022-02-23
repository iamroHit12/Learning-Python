def fun1():
    return 4+5

def fun2():
    return 4*5

def fun3():
    return abs(4-5)

def switch(arg):
    switcher = {
        1 : fun1(),
        2 : fun2(),
        3 : fun3()
    }

    return switcher.get(arg,"nothing")

if __name__ == "__main__":
    print("press 1 to add")
    print("press 2 to multiply")
    print("press 3 to subtract")
    
    print(switch(int(input())))