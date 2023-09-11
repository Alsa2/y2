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
