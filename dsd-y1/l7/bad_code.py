def hospital():
    NME=input("enter Patient Name:")
    Age =input("AGE:")
    height= input("height")
    weight= input("WEIGHT")
    bmi= float(weight)/(float(height)*float(height))
    if bmi>30:print("overweight")
    else:print("ok")
    if Age>65:print("Old person discount applied")
    print("Patient:",NME,"has bmi of",bmi)
# hospital()

def calcDiscount():
    AGE = int(input("Enter Patient age : $ "))

    if AGE > 65:
        print("Old person discount applied")

def calcBMI():
    NAME = input("Enter Patient Name: $ ")
    height = float(input("Enter Patient height : $ "))
    weight = float(input("Enter Patient weight : $ "))

    bmi = weight / (height * height)
    
    if bmi > 30:
        print("overweight")

    else:
        print("ok")

    
    print("Patient: ", NAME, " has bmi of ", bmi)

calcDiscount()
calcBMI()