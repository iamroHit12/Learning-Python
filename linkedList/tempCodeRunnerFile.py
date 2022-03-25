currNode = self.head
        while currNode is not None:
            yield (currNode.name,currNode.roll)
            currNode = currNode.next