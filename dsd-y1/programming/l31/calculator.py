import math

while True:
    userInput = float(input("Enter number $ "))
    break

print(f"Square Root: {round(math.sqrt(userInput), 2)}")
print(f"Squared: {round(math.pow(userInput, 2), 2)}")
print(f"Round up, round down: {math.ceil(userInput), math.floor(userInput)}")
print(f"Area of a cicrcle: {round(((math.pow(userInput, 2)) * math.pi), 2)}")