
def calsBurnt(time, cals_per_min):
    try:
        return float(time) * float(cals_per_min)
    except:
        return "Invalid Input"
    
def stepsToKm(steps):
    try:
        return float(steps) / 1300
    except:
        return "Imvalid Input"
    
def formatMinutes(mins):
    try:
        hours = float(mins) // 60
        minutes = round(float(mins) % 60)
        return [hours, minutes]
    except:
        return "Invalid Input"
    
def calcLeftoverMeds(meds, meds_taken):
    try:
        return round(float(meds_taken) % float(meds))
    except:
        return "Invalid Input"
    
def calcHRR(peak_heart_rate, heart_rate_after_one_minute):
    try:
        return int(peak_heart_rate) - int(heart_rate_after_one_minute)
    except:
        return "Invalid Input"

def main():
    print("""
          \n1.calcualte cals burnt on run
          \n2.convert steps to km
          \n3.turn minutes into minutes and hours
          \n4.Calculate left over meds
          \n5.calc heart rate recovery\n""")
    
    inp = input("Select option $ ")
    match(inp):
        case "1":
            print(calsBurnt(input("Enter minutes spent running $ "), input("Enter your calorie burn rate $ ")))
        case "2":
            print(calsBurnt(input("Enter steps $ ")))
        case "3":
            print(calsBurnt(input("Enter minutes $ ")))
        case "4":
            print(calsBurnt(input("Enter the amount of meds $ "), input("Enter the meds taken $ ")))
        case "5":
            print(calsBurnt(input("Enter peak heart rate $ "), input("Enter heart rate after a minute $ ")))

    main()
main()