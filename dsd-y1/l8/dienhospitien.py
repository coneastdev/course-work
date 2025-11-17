import json
#import hashlib

database = {}

# def genHash(name, age):
#     m = hashlib.sha256()
#     m.update(str(name + str(age)))
#     m.digest()
#     m.hexdigest()
#     return m

def loadDb():
    try:
        with open("patiants.json", "r") as f:
            return json.load(f)
    except:
        with open("patiants.json", "w") as f:
            f.write(json.dumps({ "test": { "pName": "name", "pAge": "age", "pHeigt": "height", "pWeight": "weight" } }))
            return { "test": { "pName": "name", "pAge": "age", "pHeigt": "height", "pWeight": "weight" } }

database = loadDb()

def calcBMI(height, weight):
    return height * (weight ** 2)

def addPatiant():
    pName = input("Enter name $ ")
    pAge = int(input("Enter age $ "))
    pHeight = None
    pWeight = None

    if input("enter weight and height? y/n $ ").lower == "y":
        pHeight = int(input("enter heigt meters $ "))
        pWeight = int(input("enter weight kilos $ "))

    with open("patiants.json", "w") as f:
        data = {}
        data = loadDb()
        data[pName] = {
            "pName": pName,
            "pAge": pAge,
            "pHeigt": pHeight,
            "pWeight": pWeight
        }
        f.write(json.dumps(data))

# addPatiant()

def printPatiant(pataint):
    data = {}
    data = loadDb()

    pd = data[pataint]

    print(f"patiatn {pd["pName"]} is {pd["pAge"]} years old.")

# printPatiant("-1")

# print(genHash("jeff", 50))