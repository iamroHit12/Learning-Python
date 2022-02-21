from os import link


class Node:
    def __init__(self,name):
        self.name = name
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAt(self,newNode,pos):
        currNode = self.head
        currPos = 0
        while True:
            if currPos == pos:
                prevNode.next = newNode
                newNode.next = currNode
                break
            prevNode = currNode
            currNode = currNode.next
            currPos =+ 1

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
                print(currNode.name)
                currNode = currNode.next

link1 = LinkedList()
f_node = Node("rohit")
s_node = Node("rahul")
t_node = Node("bittu")

link1.insert(f_node)
link1.insert(s_node)
link1.insertAt(t_node,1)

link1.printList()