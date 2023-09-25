""" D Ruben Challenge
import random
input = []
for i in range(100):
    input.append(random.randint(0, 10000))
# test the premature break if all sorted
input = [1, 2, 4, 3, 5, 6, 7, 8, 9]
"""
from Lessons import input


for i in range(len(input)):
    swapped = False
    for j in range(i + 1, len(input)):
        if input[i] > input[j]:
            input[i], input[j] = input[j], input[i]
            swapped = True
    if not swapped:
        print("ALL SORTED, BREAKING")
        print("There were " + str(i + 1) + " iterations, and " + str(len(input)-i - 1) + " elements left to sort")
        break
    print(input)
print(input)