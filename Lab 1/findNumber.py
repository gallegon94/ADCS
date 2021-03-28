import os
import sys
import random
value = random.randrange(1, 30)
current_value = 0
attempts = 0

while(current_value != value):
    current_value = input("Please enter a number:")
    print(current_value)
    if current_value == "exit":
        break
    current_value = int(current_value)
    attempts += 1
    if current_value > value:
        print("The number is smaller")
    elif current_value < value:
        print("The number is bigger")
    else:
        break

print("Got it!\n" if current_value == value else "Not found")
print("Attempts: {}".format(attempts))
with open("GuessingSteps.txt", "w") as f:
    f.write(str(attempts))
