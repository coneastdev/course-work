import datetime
import json

def checkNum():
    num = int(input("enter number"))
    if (num >= 1 and num <= 100):
        print(str(num) + " is less then 101 but more the 0")
    else:
        print(str(num) + " is more then 100 or less then 1!")
    checkNum()

# #checkNum()

def enterStudent(*args):
    if args != None:
        print(args)
    student = {
        "name": "john doe",
        "age": 0,
        "testScore": 0.0,
        "passedExam": False
    }
    student["name"] = input("enter student name $ ").upper()
    try:
        student["age"] = int(input("enter student age $ "))
    except:
        enterStudent("invalid age")
    try:
        student["testScore"] = float(input("enter student exam score $ "))
    except:
        enterStudent("invalid score")
    passed = input("Did the student pass y/n")
    if passed.lower() == "y":
        student["passedExam"] = True
    elif passed.lower() == "n":
        student["passedExam"] = False
    else:
        enterStudent("invalid input")
    
    print(f"\nThe student {student["name"]}, DOB: {datetime.datetime.now().year - student['age']}. Has recived a {"PASS" if student["passedExam"] else "FAIL"} with {student['testScore']} marks.")

# enterStudent()

def takeAttendance():
    students = { 
        "a": [0,0], # 0 = lessons, 1 = lessons missed
        "b": [0,0],
        "c": [0,0]
    }

    f = open("students.json", "r")
    students = json.load(f)
    
    studentsMissing = []
    for num, key in enumerate(students):
        inp = input(f"is {key} in class? y/n $ ").lower()
        if inp == "n":
            students[key][1] += 1
            studentsMissing += key
        students[key][0] += 1

    print(f"there are {studentsMissing} students missing.")

    f.close()
    f = open("students.json", "w")
    f.write(str(json.dumps(students)))
    f.close()
    

# takeAttendance()
