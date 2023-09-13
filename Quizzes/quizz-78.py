class Packet_Manager():
    def __init__(self, data):
        self.port = data[:16]
        self.data = data[16:]

    def check_firewall(self):
        allowed_ports = [80, 22123]
        sum = 0
        power = 1
        print(self.port)
        for i in range(15, -1, -1):
            print(self.port[i])
            sum += int(self.port[i]) * power
            power *= 2
            print(sum)
        
        if sum in allowed_ports:
            return self.data
        else:
            return None


# Test case 1: Test with allowed port
packet_manager = Packet_Manager("00000000000000000000000001010000Hello World!")
assert packet_manager.check_firewall() == "Hello World!"

# Test case 2: Test with disallowed port
packet_manager = Packet_Manager("00000000000000000000000001000000Hello World!")
assert packet_manager.check_firewall() == None

# Test case 3: Test with another allowed port
packet_manager = Packet_Manager("00000000000000000000000010101111Hello World!")
assert packet_manager.check_firewall() == "Hello World!"

# Test case 4: Test with another disallowed port
packet_manager = Packet_Manager("00000000000000000000000010100000Hello World!")
assert packet_manager.check_firewall() == None