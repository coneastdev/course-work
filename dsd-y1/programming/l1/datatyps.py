import random

myInt = 3
myFloat = 3.0
myString = "false"
myBool = False

myDic = {
    "types": {
        "string": "1",
        "int": 1,
        "bool": True
    }
}

myTup = ("x","y","z")

# print("what is the diffrence between " + str(myInt) + " and " + str(myFloat) + "?")
# print("what is the diffrence between " + str(myString) + " and " + str(myBool) + "?")

# print("what is the diffrence between " + str(myDic["types"]["string"]) + " and " + str(myDic["types"]["int"]) + "?")

# print(myDic)
# print(myTup)

# for x in range(10):
#     print(x)

# loops = 5
# print("\n")
# while loops > 0:
#     print(loops)
#     loops -= 1

# dic = [0,7,4,2,6,1,3,5,8,9,9,15,64,500,-20]
# didSomething = True
# loopsWithoutDoingSomething = 0
# while loopsWithoutDoingSomething < 3:
#     didSomething = False
#     for x in dic:
#         print(dic[x])
#         if x < (len(dic) - 1):
#             if x > dic[x + 1]:
#                 num1 = dic[x]
#                 dic[x] = dic[x + 1]
#                 dic[x + 1] = num1
#                 didSomething = True
#     if didSomething == False:
#         loopsWithoutDoingSomething += 1
#     else:
#         loopsWithoutDoingSomething = 0

# print(dic)

def myFunc(a, b):
    return a + b

def myFunk(x):
    if x < 1000000000000000:
        print(x)
        myFunk(myFunc(x, x + x))

# myFunk(1)

stuffToWrite = ""

def rngNum(x):
    return random.randrange(1, x + 2)

for x in range(100):
    # print(rngNum(x))
    stuffToWrite += str(rngNum(x))

file = open("data.json", "w")
stuffToWrite = str(stuffToWrite)
file.write("{\n\"key\":\"" + str(stuffToWrite) + "\"\n}")

file.close()

file = open("data.json", "r")

print(file.read())

file.close()