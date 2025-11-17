# medication safty rule
def canAdministerMeds(age, weight):
    try:
        if int(age) > 12 and int(weight) > 40:
            return "safe"
        else:
            return "unsafe"
    except:
        return "Invalid Input"


# fitness centre access
def canUseIntensiveZone(age, clearance):
    try:
        if int(age) >= 18 and clearance == True:
            return "Allowed into the \"Intensive Zone™\""
        else:
            return "Denied access to the \"Intensive Zone™\""
    except:
        return "Invalid Input"

# sleep tracker alert
def sendAlert(sleeping, bpm):
    try:
        if sleeping == False and bpm > 100:
            return "Alert!"
    except:
        return "Invalid Input"