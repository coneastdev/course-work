def unitConverter(*kwargs):
    # define conversion values
    MG_TO_MM = 0.0555 # divide
    MM_TO_MG = 18.018 # times

    # ask for conversion
    inp = input("1.Glucose to cletorial\n2.Cholestrial to glucose\nEnter number $ ")
    if inp == "1":
        inp = float(input("Enter MMOL/L"))
        result = inp * MM_TO_MG
        return result

    elif inp == "2":
        inp = float(input("Enter MG/DL"))
        result = inp / MG_TO_MM
        return result

# print(unitConverter())

def averageTemp():
    # define limits
    FEVER_CAP = 45
    FEVER_FLOOR = 30

    # list for the temps to be added to
    temps = []

    # add tempretures to temps until temps is 3, discard temps that reach limit
    while len(temps) < 3:
        inp = float(input("Enter temp $ "))
        if inp > FEVER_CAP:
            print(f"{inp} is too high, please ensure you type the right value.")
        elif inp < FEVER_FLOOR:
            print(f"{inp} is too low, please ensure you type the right value.")
        else:
            temps.append(inp)

    # print mean rounded to second decimal place
    print(round((sum(temps) / len(temps)), 2))

# averageTemp()


def checkHeart():
    # define values
    HEART_RATE = int(input("Enter resting heart rate $ "))
    AGE = int(input("Enter age $ "))
    MAX_HEART_BASE = 220 - AGE

    # cehck if the hear rate is normal
    if HEART_RATE > 100:
        print("High heart rate")
    elif HEART_RATE < 60:
        print("low heart rate")
    elif HEART_RATE < 101 and HEART_RATE > 59:
        print("normal heart rate")

    # print max heart rate
    print(f"the max safe heart rate is {MAX_HEART_BASE}")

    # ask if they want to go again
    if input("enter new patiant? y/n $ ") == "y":
        checkHeart()

# checkHeart()

def waterGoal():
    # define values
    WATER_INTAKE_GOAL = 3.0 # liters

    WATER_DRUNK = float(input("How much water ahve you drunk in liters? $ "))

    # if WATER_DRUNK < not enoth time :(