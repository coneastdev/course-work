import re

def calcRecSize():
    width = float(input("Enter width or rectangle $ "))
    height = float(input("Enter height of rectangle $ "))

    area = width * height

    print(f"The area of the rectangle is {area}")

# calcRecSize()

def calcMinAndHours():
    minutes = int(input("Enter minutes $ "))
    
    hours = minutes // 60
    minutes -= (60 * hours)

    print(f"The time is {hours}(s) and {minutes} minute(s).")

# calcMinAndHours()

def calcVAT():
    VAT_Rate = 1.2 # 20%

    GROSS_Income = float(input("Enter GROSS income $ "))
    Taxed_Income = GROSS_Income * VAT_Rate

    print(f"The tax added income is {Taxed_Income}, you have to pay {Taxed_Income - GROSS_Income} in taxes")

# calcVAT()

def billPatiant():
    try:
        CHILD_DISCOUNT_RATE = 0.80 # 20% off
        VAT_RATE = 1.20 # 20%

        age = int(input("Enter age $ "))
        name = input("Enter name $ ")
        bill = float(input("Enter bill $ "))

        if age < 18:
            bill *= CHILD_DISCOUNT_RATE
        
        bill *= VAT_RATE


        print(f"Patiant {name} whom is a {"child, entiteld to a 20% discount" if age < 18 else "adult"}, has a total bill of {round(bill, 2)}")

    except:
        print("Invalid input, please try again")
        billPatiant()

# billPatiant()

def passCheck():
    try:
        pass_word = input("Enter a password thats more then 8, has a capital and number $ ")
        if len(pass_word) >= 8 and pass_word != pass_word.lower() and int(pass_word) != "" and re.sub(r'\d+', '', pass_word) != "":
            print("valid password")
        else:
            print("invalid password try again")
            passCheck()
    except:
        print("invalid password try again")
        passCheck()

# passCheck() dsont work for some reason i blame reg ex

#def menu():

def patMenu():
    while True:
        print("select menu\n1.add patiant detatils\n2.calculate BMI\n3.check doasge\n4.exit")
        inp = input("selet menu option $ ")
        if inp == "1":
            input("this is a patiant deatil screen, press enter to exit back to main menu")
        elif inp == "2":
            input("this is a patiant BMI calc screen, press enter to exit back to main menu")
        elif inp == "3":
            input("this is a patiant dosage checking screen, press enter to exit back to main menu")
        elif inp == "4":
            break

patMenu()