import json
from datetime import datetime

data = []


def readData():
    with open("loans.json", "r") as f:
        return json.load(f)
    
def writeData():
    with open("loans.json", "w") as f:
        f.write(json.dump(data))
    
def modify(id):
    for loan in data:
        if id == loan("laonID"):
            print(f"\n{loan["loanID"]}. {loan["userName"]} ({loan["userID"]}) {loan["deviceType"]} [{loan["lent"]}] / [{loan["due"]}] ({loan["deviceID"]}) returned:{loan["returned"]}")
            print("\nwhat would you like to change?\n1. return\n2. student details\n3. dates\n4. device\n5. deleate entry\n")
            selection = input("Enter option number $ ")
            match selection:
                case "1":
                    if input("Has the device been returend Y/n? $ ").lower == "y":
                        loan["returned"] = "True"
                    else:
                        loan["returned"] = "False"

                case "2":
                    loan["userID"] = input("Enter the new student ID $ ")
                    loan["userName"] = input("Enter the new name $ ")

                case "3":
                    loan["lent"] = input("Enter lent date, (YYYY/MM/DD) $ ")
                    loan["due"] = input("Enter due date, (YYYY/MM/DD) $ ")

                case "4":
                    loan["deviceID"] = input("Enter the device ID (\"L-\"+3 numbers) $ ")
                    loan["deviceType"] = input("Enter the device type $ ").lower()
                
                case "5":
                    if input("Are you sure you want to delete this entry? Y/n $ ").lower() == "y":
                        data.pop(loan)

        

def view():
    print("")
    for loan in data:
        if loan["returned"] == "False":
            due = datetime.strptime(loan["due"], '%Y-%m-%d')
            now = datetime.now()
            if due < now:
                print(f"\033[0;31m{loan["loanID"]}. {loan["userName"]} ({loan["userID"]}) {loan["deviceType"]} {loan["due"]} (due)\033[0m")
            else:
                print(f"{loan["loanID"]}. {loan["userName"]} ({loan["userID"]}) {loan["deviceType"]} {loan["due"]}")
    selection = input("enter id to modify or enter to return $ ")
    if selection != "":
        print("")

def search():
    print("To search enter one of the following\n\n. loan id (numbers)\n. student ID (\"S\"+numbers)\n. student name (letters)\n. device ID (\"L-\"+3 numbers)\n")
    selection = input("Enter ")
    chrs = list(selection)
    results = []
    if str(chrs[0]).isnumeric(): # loan id
        for loan in data:
            if str(loan["loanID"]) == selection:
                results.append(loan)
    elif str(chrs[0]).capitalize() == "S" and str(chrs[1]).isnumeric(): # student id
        for loan in data:
            if str(loan["userID"]) == selection.capitalize():
                results.append(loan)
    elif str(chrs[0]).capitalize() == "L" and str(chrs[1]) == "-" and str(chrs[2]).isnumeric(): # device id
        for loan in data:
            if loan["deviceID"] == selection.capitalize():
                results.append(loan)
    else: # student name
        for loan in data:
            if selection in str(loan["userName"]).lower():
                results.append(loan)
    
    print("")
    for loan in results:
        due = datetime.strptime(loan["due"], '%Y-%m-%d')
        now = datetime.now()
        if due < now:
            print(f"\033[0;31m{loan["loanID"]}. {loan["userName"]} ({loan["userID"]}) {loan["deviceType"]} [{loan["lent"]} / {loan["due"]}] ({loan["deviceID"]}) returned:{loan["returned"]} (due)\033[0m")
        else:
            print(f"{loan["loanID"]}. {loan["userName"]} ({loan["userID"]}) {loan["deviceType"]} [{loan["lent"]}] / [{loan["due"]}] ({loan["deviceID"]}) returned:{loan["returned"]}")
    selection = input("enter id to modify or enter to return $ ")
    if selection != "":
        print("")

def add():
    print()

def main():
    print("##### device loan manager #####")
    print("1.view loans\n2.search\n3.add")
    select = input("enter selection number $ ")
    match select:
        case "1":
            view()
        case "2":
            search()
        case "3":
            add()
    main()

if __name__ == "__main__":
    try:
        data = readData()
    except:
        f = open("loans.json", "w")
        f.write("[]")
        f.close()
        data = readData()
    
    main()
    