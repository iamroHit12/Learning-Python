from matplotlib.pyplot import flag


class node:
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
            print("no record")
        else:
            currNode = self.head
            while currNode is not None:
                print(currNode.data)
                currNode = currNode.next

    def delNOde(self):
        lastNode = self.head
        while lastNode.next is not None:
            temp = lastNode
            lastNode = lastNode.next
        temp.next = None

    def delValue(self,val):
        lastNode = self.head
        currNode = self.head
        while currNode is not None:
            flag = False
            if(val == currNode.data):
                flag = True
                break
            currNode = currNode.next

        if(flag):
            while lastNode is not None:
                if(lastNode.data == val):
                    temp = lastNode.next
                    break
                else:
                    temp1 = lastNode
                lastNode = lastNode.next
            temp1.next = temp
            print("\n---after deletion---")
            link1.printList()
        else:
            print("\nvalue does not match")

link1 = LinkedList()

f_node = node(1)
s_node = node(2)
t_node = node(3)
fo_node = node(4)
fi_node = node("rohit")

link1.insert(f_node)
link1.insert(s_node)
link1.insert(t_node)
link1.insert(fo_node)
link1.insert(fi_node)

link1.printList()

#link1.delNOde()
link1.delValue("rohi")
#link1.printList()