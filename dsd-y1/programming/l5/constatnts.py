import json
import random
import os

def calc_BMI(height, weight):
    bmi = (weight / (height ** 2))
    print(f"the BMI is {bmi}")
    if bmi <= 18.5:
        return "Too skiny eat milk"
    elif bmi <= 24.9:
        return "You fine"
    elif bmi <= 29.9:
        return "You fat pig"
    elif bmi <= 39.9:
        return "Are you american or somthing???"
    elif bmi > 40:
        return "You are going to die soon..."
    else:
        return "ERROR, invalid BMI"

#print(calc_BMI(1.8288, 90))

def task1():
    name = input("Enter patiatnts name $ ")
    DOB = input("Enter patiatnts date of birth $ ")
    NHIS = input("Enter NHS number $ ")
    POST_CODE = input("Enter post code $ ")
    height = float(input("Enter patiatnts height in meters $ "))
    weight = float(input("Enter patiatnts wieght in kilos $ "))

    print(f"{name} was born in {DOB}, their NHS number is {NHIS} and their postcode is {POST_CODE}. Their wieght is {weight} kilos and height {height} meters, BMI being {calc_BMI(height, weight)}.")

# task1()

def logPataintDosage(): # is broke not egnoth time to debug :(
    DALIY_DOSAGE_LIMIT = 5.3 # ml
    PATAINT = input("Enter pataint name $ ")
    f = open("patiants.json", "r")
    pataitns = json.load(f)
    f.close()
    DOSAGES = sum(pataitns[PATAINT]["dosages"])
    DOSE = float(input("Enter dose to administer in ml $ "))
    if DOSAGES + DOSE > DALIY_DOSAGE_LIMIT:
        print("YOU CANNOT ADIMISTER THE DOSE AS IT WOULD EXCEAD THE DALITY LIMIT")
    elif DOSAGES + DOSE <= DALIY_DOSAGE_LIMIT:
        print("You are safe to administer the dose")
        #pataitns[PATAINT]["dosages"] = DOSE
        f = open("patiants.json", "r+")
        jayson = json.load(f)
        jayson[PATAINT]["dosages"] += DOSE
        f.write("")
        f.write(json.dumps(jayson))
        f.close()
    else:
        print("error computing please seek help before administering a dose")


def calcCosts():
    ROOM_PRICE_PER_DAY = 50
    TREATMENT_COST = random.randint(30, 3000)
    CONSULTATION_HOUR_COST = random.randint(30, 300)

    DAYS_IN_ROOM = int(input("If they stayed in a room how many days where they in in for? $ "))
    TREATMENTS = int(input("If they recived treatment how many? $ "))
    CONSULTATIONS = int(input("If they recived a consultation how long did it last? $ "))

    COST = (DAYS_IN_ROOM * ROOM_PRICE_PER_DAY) + (TREATMENTS * TREATMENT_COST) + (CONSULTATIONS * CONSULTATION_HOUR_COST)
    VAT = COST * 0.20
    TOTAL_COST = COST + VAT

    print(f"The bill is £{COST} with vat being £{VAT} equaling a combined cost of £{TOTAL_COST}.")

# calcCosts()

def main():
    print("Select function\n1.bmi calc\n2.task1\n3.logdose(not working)\n4.calc cost")
    inp = input("Enter number to selecet $ ")
    if inp == "1":
        print(calc_BMI(float(input("Enter height in meters $ ")),float(input("enter weight in kilos $ "))))
    elif inp == "2":
        task1()
    elif inp == "3":
        logPataintDosage()
    elif inp == "4":
        calcCosts()
    else:
        print("invalid input")
    input("press enter to clear screen")
    os.system("cls")
    main()
main()