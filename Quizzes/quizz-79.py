import time

class Palindrome_Finder:
    def __init__(self):
        pass

    def palidrome_check(self, num_list):
        for i in range(len(num_list)//2):
            if num_list[i] != num_list[-i-1]:
                return False
        return True

    def find_palindromes(self, a, b):
        palindromes = []
        for i in range(a, b+1):
            if self.palidrome_check(list(str(i))):
                palindromes.append(i)
        return palindromes
    
if __name__ == "__main__":
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))
    time_start = time.time()
    pf = Palindrome_Finder()
    time_end = time.time()
    print(pf.find_palindromes(a, b))
    print("Time taken: ", time_end - time_start)