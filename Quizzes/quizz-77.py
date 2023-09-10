class Packet_corrector:
    def __init__(self, data):  # data split into 3 parts
        self.data = []
        self.data.append(data[0:len(data)//3])
        self.data.append(data[len(data)//3:2*len(data)//3])
        self.data.append(data[2*len(data)//3:len(data)])
        return
    def parity_check(self, data):
        check = int(data[0])
        data = data[1:]
        count = 0
        for i in data:
            if i == '1':
                count += 1
        if count % 2 == check:
            return True
        else:
            print("Error in data: ", data)
            return False
        
    def correct(self):
        # return the correct data only
        output = ""
        for i in self.data:
            if self.parity_check(i):
                return i[1:]
    
    
test = Packet_corrector('100111001011001110010110011100101')
print(test.correct())

"""
class Packet_corrector:
    def __init__(self, data):
        self.data = [data[i:i+len(data)//3] for i in range(0, len(data), len(data)//3)]
        
    def parity_check(self, data):
        check = int(data[0])
        count = data[1:].count('1')
        return count % 2 == check
        
    def correct(self):
        for i in self.data:
            if not self.parity_check(i):
                print("Error in data: ", i[1:])
                return None
        return ''.join([i[1:] for i in self.data])
    
test = Packet_corrector('100111001011001110010110011100101')
print(test.correct())
"""