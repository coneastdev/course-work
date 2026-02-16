import random

lives = 3

dice = {"min": 1, "max": 6}
amntOfDices = 2
dices = []
winingTotals = [7, 11]

while lives > 0:
    print(f"Lives: {lives}")
    if input("roll? Y/n $ ").lower() == "y":
        dices = []
        for d in range(amntOfDices):
            val = random.randrange(dice["min"], dice["max"])
            dices.append(val)
            print(val)

        print(f"the sum is {sum(dices)}")

        if sum(dices) in winingTotals:
            break
        else:
            lives -= 1
    else:
        quit()

if lives > 0:
    print("You win!")
else:
    print("You fail...")