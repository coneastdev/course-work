# 1
def calcStepGoal(steps, goal):
    try:
        # calc persentage of goal achived
        percent_of_goal  = int((float(steps) / float(goal)) * 100)

        # ensure it is a valid percentage
        if percent_of_goal > 100:
            percent_of_goal = 100
        elif percent_of_goal < 0:
            percent_of_goal = 0

        # calcualte remaining steps
        remaining_steps = int(goal) - int(steps)

        # ensure remaining steps isnt negative
        if remaining_steps < 0:
            remaining_steps = 0

        # return pernectage left and steps left
        return f"You have achived {percent_of_goal}% of your goal and have {remaining_steps} steps left, keep it up!"
    except:
        return "Invalid Input"
    
# print(calcStepGoal(60, 215)) # outputs You have achived 27% of your goal and have 155 steps left, keep it up!

# 2
def CalcBMI(weight_kg, height_m):
    try:
        # calculate bmi index
        bmi = float(weight_kg) / (float(height_m) ** 2)

        # return weight group
        if bmi < 18.5:
            return "under weight"
        elif bmi < 25:
            return "Healthy"
        elif bmi < 30:
            return "Overweight"
        elif bmi >= 30:
            return "Obse"
        else:
            return f"{bmi} is an invalid BMI"
    except:
        return "Invalid Input"

# print(CalcBMI(90, 1.8)) # outputs Overweight

#3
def flagUser(daily_screen_minutes, night_screen_minutes, steps):
    try:
        # check they arnt overusing a screen
        if (int(daily_screen_minutes) > 240 and int(steps) < 5000) or (int(night_screen_minutes) > 60):
            # flag the user
            return True
        else:
            # do not flag the user
            return False
    except:
        return "Invalid Input"
    
# print(flagUser(568, 10, 4999)) # outputs True, if steps = 500 outputs False

# 4
def calcHydrationPoints(water_ml):
    try:
        # calc points per 250
        points = water_ml // 250

        # calc points per 2000
        points += ((water_ml // 2000) * 5)

        return points
    except:
        return "Invalid Input"
    
# print(calcHydrationPoints(3250)) # outputs 18

# 5
def eligibleForFreeClass(age, low_income, days_since_last_free):
    try:
        # calcualte eligablity
        if ((age >= 16 and age <= 25) or low_income == True) and (days_since_last_free > 30):
            # not eligable
            return True
        else:
            # eligable
            return False
    except:
        return "Invalid Input"

# print(eligibleForFreeClass(16, False, 36)) # outputs True

# 6
def weeklyTier(steps, water_ml):
    try:
        # calculate points
        points = (float(steps) // 1000) * 2 + (float(water_ml) // 500)

        # calculate tier
        if points < 20:
            return "Bronze"
        elif points < 40:
            return "Silver"
        elif points >= 40:
            return "Gold"
        else:
            return f"{points} is an invalid point value"
    except:
        return "Invalid Input"

print(weeklyTier(10000, 9000)) # outputs Silver

# 7

# 8