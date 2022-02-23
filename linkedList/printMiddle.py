class Node:
    def __init__(self,data):
        self.data = data
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
                print(currNode.data)
                currNode = currNode.next

    def printmid(self):
        if self.head is None:
            print("No record")
        else:
            currNode = self.head
            count = 0
            while currNode is not None:
                count += 1
                currNode = currNode.next

            currNode = self.head
            for i in range(count//2):
                currNode = currNode.next
            print(currNode.data)

link1 = LinkedList()
f_Node = Node(1)
s_Node = Node(2)
t_Node = Node(3)
fo_Node = Node(4)
fi_Node = Node(5)
si_node = Node(6)

link1.insert(f_Node)
link1.insert(s_Node)
link1.insert(t_Node)
link1.insert(fo_Node)
link1.insert(fi_Node)
link1.insert(si_node)

link1.printList()
print("---middle element---\n")
link1.printmid()