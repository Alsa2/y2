class ascii_to_binary():
    def __init__(self, text):
        output = ""
        for i in text:
            i = ord(i)
            binary = ""
            for j in range(8):
                binary += str(i % 2)
                i //= 2
            output += binary[::-1]
            output += " "
        self.output = output

    def __str__(self):
        return str(self.output)

if __name__ == "__main__":
    text = input("Enter text: ")
    print(ascii_to_binary(text))
