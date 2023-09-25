class collections:
    def __init__(self) -> None:
        self.data = []
        self.location = 0
        pass

    def addItem(self, item):
        self.data.append(item)
        pass

    def isEmpty(self)->bool:
        return len(self.data) == 0
    
    def hasNext(self)->bool:
        return self.location < len(self.data) - 1
    
    def getNext(self):
        if self.hasNext():
            temp = self.data[self.location]
            self.location += 1
            return temp
        else:
            raise Exception("No more items in collection")
    

class queue():
    def __init__(self) -> None:
        self.data = []
        pass
    def enqueue(self, item):
        self.data.append(item)
        pass
    def dequeue(self):
        item = self.data[0]
        self.data = self.data[1:]
        return item

if __name__ == "__main__":
    c = collections()
    c.addItem(1)
    c.addItem("Hello")
    print(c.isEmpty())
    print(c.getNext())
    print(c.getNext())