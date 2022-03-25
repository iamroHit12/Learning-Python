class Node:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            lastNode = self.head
            while lastNode.next is not None:
                lastNode = lastNode.next
            lastNode.next = newNode

    def printList(self):
        if self.head is None:
            print("NO record")
        else:
            currNode = self.head
            while currNode is not None:
                print(currNode.name,currNode.roll)
                currNode = currNode.next

link1 = LinkedList()

def inputVal():
    name = input("enter name : ")
    roll = int(input("enter roll : "))
    link1.insert(Node(name,roll))
    print("Successfully Saved")

def showList():
    print("----- here is list -----")
    link1.printList()

def showMenu():
    print("1 to insert")
    print("2 to show")
    print("3 to exit")

if __name__ == "__main__":
    showMenu()
    
    while True:
        opt = int(input("enter option : "))

        if opt == 1:
            inputVal()
        elif opt == 2:
            showList()
        elif opt == 3:
            print("thank you for using this service")
            exit()
        else:
            print("wrong input")