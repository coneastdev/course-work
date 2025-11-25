import json
from datetime import datetime

data = []

def readData():
    with open("loans.json", "r") as f:
        return json.load(f)
    
def writeData():
    with open("loans.json", "w") as f:
        f.write(json.dump(data))
    
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

def modify():
    print()

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
    input("\npress enter to continue | ")
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
    