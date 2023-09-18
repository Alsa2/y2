class Average_Calculator():
    def __init__(self, values) -> None:
        self.values = values
        pass

    def Average_1(self):
        output = 0
        for i in self.values:
            output += float(i)
        return output / len(self.values)
    
    def Average_2(self):
        output = 0
        for i in self.values:
            output += float(i) / 7
        return output
    
    def Average_3(self):
        return sum(self.values) / len(self.values)
