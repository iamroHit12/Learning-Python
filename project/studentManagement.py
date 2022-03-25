from os import link


class Node:
    def __init__(self,name,roll,sec):
        self.name = name
        self.roll = roll
        self.sec = sec
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

    def searchNode(self,roll):
        if self.head is None:
            print("No record")
        else:
            currNode = self.head
            while currNode is not None:
                if(currNode.roll == roll):
                    print("\n")
                    print(str.capitalize(currNode.name),currNode.roll,str.upper(currNode.sec))
                    break
                elif(currNode.roll != roll):
                    print("\nNo match found")
                currNode = currNode.next

    def delValue(self,roll):
        temp = self.head

        # if head node has key
        if temp is not None:
            if temp.roll == roll:
                self.head = temp.next
                temp = None
                return

        # if head node has not key

        while temp is not None:
            if temp.roll == roll:
                break
            prev = temp
            temp = temp.next

        # if key was not there
        if temp == None:
            print("\nNo such roll is there")
            return

        prev.next = temp.next
        temp = None


    def printList(self):
        if self.head is None:
            print("NO record")
        else:
            currNode = self.head
            while currNode is not None:
                print(str.capitalize(currNode.name),currNode.roll,str.upper(currNode.sec))
                currNode = currNode.next

link1 = LinkedList()

def inputValue():
    name = input("Name : ")
    roll = int(input("Roll : "))
    sec = input("Section : ")
    link1.insert(Node(name,roll,sec))
    print("\nSuccessfully Saved")

def showList():
    print("\nHere is List\n")
    link1.printList()

def search():
    roll = int(input("\n Enter Roll to find : "))
    link1.searchNode(roll)

def removeNode():
    roll = int(input("\n Enter Roll to delete : "))
    link1.delValue(roll)

def menu():
    print("----- Student Record -----\n")
    print("Press 1 to add details")
    print("Press 2 to show List")
    print("Press 3 to search in record")
    print("Press 4 to delete in record")
    print("press 5 to EXIT")

if __name__ == "__main__":
    menu()

    while True:
        option = int(input("\nEnter your option : "))

        if option == 1:
            inputValue()
        elif option == 2:
            showList()
        elif option == 3:
            search()
        elif option == 4:
            removeNode()
        elif option == 5:
            exit()
        else:
            print("Invalid Input")