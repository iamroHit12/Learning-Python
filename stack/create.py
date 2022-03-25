class Stack:
    def __init__(self):
        self.stack = []

    def push(self,val):
        self.stack.append(val)

    def remove(self):
        if len(self.stack) <= 0:
            print("stack is empty")
        else:
            self.stack.pop()
            print("\nlast item removed")

    def peek(self):
        print(self.stack)

stack1 = Stack()

def add():
    val = input("\nenter value : ")
    stack1.push(val)


def showMenu():
    print("1. Push")
    print("2. remove")
    print("3. peek")
    print("4. Exit")

if __name__ == "__main__":
    showMenu()
    while True:
        choice = int(input("\nenter choice : "))

        if choice == 1:
            add()
        elif choice == 2:
            stack1.remove()
        elif choice == 3:
            stack1.peek()
        elif choice == 4:
            exit()
        else:
            print("wrong input")