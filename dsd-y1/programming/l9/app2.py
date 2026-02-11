
def calcConcertration(mass, volume):
    try:
        return float(mass) / float(volume)
    except:
        return "Invalid Input"
    
def doseByWeight(dose, weight):
    try:
        return float(dose) * float(weight)
    except:
        return "Invalid Input"
    
def calcIdealBodyWeight(gender, height):
    try:
        if gender == "f" or gender == "female":
            f = 45.5
        elif gender == "m" or gender == "male":
            f = 50
        return f + 0.91 * (height - 152)
    except:
        return "Invalid Input"

# def main():
#     looping = True
#     while looping:
        

# if __name__ == "__main__":
#     main()