class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertHead(self,newNode):
        temp = self.head
        self.head = newNode
        self.head.next = temp
        del temp

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
            print("List is empty")
        
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode = currentNode.next

linkedList = LinkedList()

firstNode = Node("Rohit")
secondNode = Node("Bittu")
thirdNode = Node("Rahul")
forthNode = Node("Bunty")

linkedList.insert(firstNode)
linkedList.insert(secondNode)
linkedList.insert(thirdNode)
linkedList.insertHead(forthNode)

linkedList.printList()