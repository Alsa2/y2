import random

class ipv6machine:
    def __init__(self, N:int):
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        self.output = set()
        while len(self.output) < N:
            temp = ""
            for i in range(8):
                for j in range(4):
                    temp += random.choice(values)
                if i != 7:
                    temp += ":"
            self.output.add(temp)

        return
    def __str__(self):
        return str(self.output)
    
print (ipv6machine(1000000))