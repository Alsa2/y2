import random
import pytest

class ipv6machine():
    def __init__(self, number):
        self.number_wanted = int(number)

    def create_ipv6_address(self):
        hex_chars = "0123456789abcdef"

        def generate_address():
            return ":".join(''.join(random.choice(hex_chars) for _ in range(4)) for _ in range(8))

        output = set()
        while len(output) < self.number_wanted:
            output.add(generate_address())

        return output

    def dec2hex(self, digit):
        hex_dig = "abcdef"
        if digit < 16:
            if digit < 10:
                return str(digit)
            else:
                return hex_dig[digit - 10]
        return None

    def get_rand_hex(self):
        return self.dec2hex(random.randint(0, 15))

    def sixtect_hex(self):
        group = ""
        for _ in range(4):
            group += self.get_rand_hex()
        return group
    
def test_ipv6machine():
    ipv6 = ipv6machine(5)
    addresses = ipv6.create_ipv6_address()
    assert len(addresses) == 5
    for address in addresses:
        assert len(address.split(":")) == 8
        for group in address.split(":"):
            assert len(group) == 4
            for char in group:
                assert char in "0123456789abcdef"