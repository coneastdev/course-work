# x = 25
# y = 3.14
# print(type(x), type(y))

# ints are better then floats becuse they take less bits

# a = 10
# b = 3
# print(a / b)
# print(a // b)
# print(a * 2.5)

def average():
    print("\nEnter your scores with spaces in between")
    inp = input("enter scores $ ")

    testScores = inp.split(" ")

    totalTestScores = 0

    for s in testScores:
        totalTestScores += int(s)

    print("\nThe average score is " + str(totalTestScores / len(testScores)))
    average()

#main()

# var1 = 1
# var2 = 2
# opperater = "+"

def calcualtor(var1, var2, opperator):
    print("Welcome to the menu\n\n1.varible 1\n2.varible 2\n3.opperator\n4.execute\n\ncurrent selection\nvar 1 = " + str(var1) + "\nvar 2 = " + str(var2) + "\nopperator = " + str(opperater) + "\n")
    inp = input("select number $ ")
    if inp == "1":
        print("\nSelect option\n1.add\n2.minus\n3.times\n4.divide")
        inp = input("select number $ ")
        if inp == "1": # varible 1
            var1 += int(input("enter number to add $ "))
        elif inp == "2":
            var1 -= int(input("enter number to minus $ "))
        elif inp == "3":
            var1 *= int(input("enter number to times $ "))
        elif inp == "4":
            var1 /= int(input("enter number to divide $ "))

    elif inp == "2": # varible 2
        print("\nSelect option\n1.add\n2.minus\n3.times\n4.divide")
        inp = input("select number $ ")
        if inp == "1":
            var2 += int(input("enter number to add $ "))
        elif inp == "2":
            var2 -= int(input("enter number to minus $ "))
        elif inp == "3":
            var2 *= int(input("enter number to times $ "))
        elif inp == "4":
            var2 /= int(input("enter number to divide $ "))

    elif inp == "3": # opperator
        print("\nSelect option\n+ - * /")
        inp = input("select number $ ")
        if inp == "+":
            opperater = "+"
        elif inp == "-":
            opperater = "-"
        elif inp == "*":
            opperater = "*"
        elif inp == "/":
            opperater = "/"

    elif inp == "4": # execute
        output = 0
        if opperater == "+":
            output = var1 + var2
        elif opperater == "-":
            output = var1 - var2
        elif opperater == "*":
            output = var1 * var2
        elif opperater == "/":
            output = var1 / var2

        print(output)
        var1 = output
        var2 = output * 2

    calcualtor()

# calcualtor(1, 2, "+")

def greeter():
    name = "Alex"
    greeting = "Hello " + name
    print(greeting)
    print(name.upper(), len(name))

def getName():
    first = input("Enter First Name $ ")
    last = input("Enter Last Name $ ")
    fullname = (first + last)
    if len(fullname) > 20:
        print("ERROR, Your fullname is to long, please enter a shortened version below 20 chracters.")
        getName()

# getName()