import datetime

currentDate = datetime.datetime.now()

print(f"The curruent date is: {currentDate.strftime('%d/%m/%Y')}")

while True:
    dob = input("enter your date of birth in the format of (DD/MM/YYYY) $ ")
    dob = datetime.datetime.strptime(dob, '%d/%m/%Y')
    break

print(f"Your date of birth is: {dob}")

age = currentDate - dob

print(f"You are {age.days // 365} years old")

birthdayMonth = dob.month
birthdayDay = dob.day

currentYear = currentDate.year
currentMonth = currentDate.month
currentDay = currentDate.day

if birthdayDay == currentDay and birthdayMonth == currentMonth:
    print("Happy birthday!")
    nextBirthdayYear = currentYear + 1

elif birthdayMonth == currentMonth:
    if birthdayDay > currentDay:
        nextBirthdayYear = currentYear
    else:
        nextBirthdayYear = currentYear + 1

else:
    nextBirthdayYear = currentYear

nextBirthday = datetime.datetime.strptime(f"{birthdayDay}/{birthdayMonth}/{nextBirthdayYear}", '%d/%m/%Y')
daysTillBirthDay = nextBirthday - currentDate

print(f"your next birthday is {nextBirthday.strftime('%d/%m/%Y')}, thats {daysTillBirthDay.days} days to go")