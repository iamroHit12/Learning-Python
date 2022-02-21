class node:
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
            print("No record")
        else:
            currNode = self.head

            while currNode is not None:
                print(currNode.roll)
                currNode = currNode.next

link1 = LinkedList()

firstNode = node("Rohit",12)
secNode = node("Rahul",13)

link1.insert(firstNode)
link1.insert(secNode)

link1.printList()