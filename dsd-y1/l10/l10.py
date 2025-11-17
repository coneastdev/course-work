# g = 6
# if g > 7.0:
#     print("more then 7")

# h = 59
# if h == 70: 
#     print("70")

# o = 80
# if o < 95:
#     print("95")

def checkTemp(tempreture):
    try:
        if float(tempreture) > 37.5:
            return "High tempreture"
        elif float(tempreture) < 34.5:
            return "Low tempreture"
        else:
            return "Normal tempreture"
    except:
        return "Invalid Input"
    
def checkOxygen(oxygen_level):
    try:
        if float(oxygen_level) > 100:
            return "Invalid Input"
        elif float(oxygen_level) < 92:
            return "Low oxygen"
        else:
            return "Normal oxygen"
    except:
        return "Invalid Input"
    
def checkHeart(heart_rate):
    try:
        if int(heart_rate) > 100:
            return "High heart rate"
        elif int(heart_rate) < 60:
            return "Low heart rate"
        else:
            return "Normal heart rate"
    except:
        return "Invalid Input"

def checkVitals():
    tempreture = checkTemp(input("Enter patiant tempreture $ "))
    if tempreture == "Invalid Input":
        print("\nInvalid Input, please try again\n")
        checkVitals()

    oxygen_level = checkOxygen(input("Enter patiant oxygen level $ "))
    if oxygen_level == "Invalid Input":
        print("\nInvalid Input, please try again\n")
        checkVitals()

    heart_rate = checkHeart(input("Enter patiant heart rate $ "))
    if heart_rate == "Invalid Input":
        print("\nInvalid Input, please try again\n")
        checkVitals()
    
    print(f"The pataints has a {tempreture}, {oxygen_level} and {heart_rate}.")

    if input("Would you like to check another patiatn, Y/N $ ").lower() == "y":
        checkVitals()


checkVitals()

    

#
# a single = is used to assign
# a double == is used to compare
# >= is more then or equal to, you could use this in cheking if someone is 18 or over to see if their an adult
# you can use arithmitic and relational together in the same if statement
#