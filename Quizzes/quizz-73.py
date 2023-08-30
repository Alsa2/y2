import pytest

class MacManager():
    def __init__(self) -> None:
        self.table = {}
        #range of ip addresses is 192.168.0.0/24
        self.available = 256
        return
    def check_mac(self, mac:str) -> bool:
        # check if format is correct
        if len(mac) != 17:
            return False
        if mac[2] != ":" or mac[5] != ":" or mac[8] != ":" or mac[11] != ":" or mac[14] != ":":
            return False
        # check if all characters are valid
        values = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        for i in range(17):
            if i == 2 or i == 5 or i == 8 or i == 11 or i == 14:
                continue
            if mac[i] not in values:
                return False
        return True
    
    def add_mac(self, mac:str) -> None:
        if self.check_mac(mac):
            self.table[mac] = True
            ip = str("192.168.0." + str(256 - self.available))
            self.available -= 1
            self.table[mac] = ip
        return
    def get_ip(self, mac:str) -> str:
        if self.check_mac(mac):
            return self.table[mac]
        return "invalid mac address"
    

def test_mac_manager():
    # test if mac address is valid
    mac_manager = MacManager()
    assert mac_manager.check_mac("00:00:00:00:00:00") == True
    assert mac_manager.check_mac("00:00:00:00:00:0g") == False
    assert mac_manager.check_mac("00:00:00:00:00:0") == False
    assert mac_manager.check_mac("00:00:00:00:00:000") == False
    assert mac_manager.check_mac("0::00:00:00:00:00") == False

    # test if mac address is added to table
    mac_manager.add_mac("00:00:00:00:00:00")
    assert mac_manager.get_ip("00:00:00:00:00:00") == "192.168.0.0"
    mac_manager.add_mac("00:00:00:00:00:01")
    assert mac_manager.get_ip("00:00:00:00:00:01") == "192.168.0.1"

    # test if invalid mac address is added to table
    mac_manager.add_mac("00:00:00:00:00:0g")
    assert mac_manager.get_ip("00:00:00:00:00:0g") == "invalid mac address"

if __name__ == "__main__":
    wifi = MacManager()
    wifi.add_mac("00:00:00:00:00:00")
    print(wifi.get_ip("00:00:00:00:00:00"))
    wifi.add_mac("00:00:00:00:00:01")
    print(wifi.get_ip("00:00:00:00:00:01"))

    
    