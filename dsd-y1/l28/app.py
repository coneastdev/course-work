import pandas as pd

studentData = {
    "name": ["Alex", "Jamie", "Sam"],
    "attendance": [92, 85, 78],
    "grade": ["B", "C", "D"]
}

df = pd.DataFrame(studentData)
print(df)

newStudent = {
    "name": "Jeff",
    "attendance": [43],
    "grade": ["F"]
}

newStudentDf = pd.DataFrame(newStudent)

df = pd.concat([df, newStudentDf], ignore_index=True)

print(df)

passed = [True, True, False, False]

df.insert(3, "passed", passed)

print(df)