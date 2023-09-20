class my_collections:
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

a = my_collections()
a.addItem("bob")
a.addItem("alice")
a.addItem("zoe")
a.addItem("charlie")

# transform the collection into a list
input = []
while a.hasNext():
    input.append(a.getNext())
print(input)

for i in range(len(input)):
    for j in range(i + 1, len(input)):
        if input[i] > input[j]:
            input[i], input[j] = input[j], input[i]
print(input)

