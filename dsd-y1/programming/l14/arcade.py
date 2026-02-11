machines  = ["Pinball Wizard", "Dance Floor X", "Retro Racer", "Alien Blaster"]
categories = ["Pinball", "Rhythm", "Racing", "Shooter"]
status     = ["Working", "Working", "Needs Service", "Working"]

while True:
    print("----- arcade machines index -----\n1. view machines\n2. add machine\n3. remove machine\n4. change machine status\n5. search by category\n6. list machines needing service\n7. exit")
    inp = input("select option $ ")
    print("")
    match inp:
        case "1":
            for i,v in enumerate(machines):          
                print(f"{i + 1}. {v} ({categories[i]}) <{status[i]}>")
            input("\n press enter to continue")
        case "2":
            machines.append(input("enter game name $ "))
            categories.append(input("enter game categories $ "))
            print("\nselect status\n1. working\n2. needs service\n3. out of order\n")
            statusInp = input("enter status number $ ")
            if statusInp == "1": 
                statusInp = "Working" 
            elif statusInp == "2": 
                statusInp = "Needs Service"
            elif statusInp == "3":
                statusInp = "Out of order"
            status.append(statusInp)
            print(f"{machines[-1]} added to games")
            input("\n press enter to continue")
        case "3":
            for i,v in enumerate(machines):
                print(f"{i + 1}. {v} ({categories[i]}) <{status[i]}>")
            inp = input("enter index $ ")
            try:
                machines.pop(int(inp) - 1)
                categories.pop(int(inp) - 1)
                status.pop(int(inp) - 1)
            except:
                print("index not found")
            input("\n press enter to continue")
        case "4":
            for i,v in enumerate(machines):
                print(f"{i + 1}. {v} ({categories[i]}) <{status[i]}>")
            inp = input("enter index $ ")
            print("\nselect status\n1. working\n2. needs service\n3. out of order\n")
            statusInp = input("enter status number $ ")
            if statusInp == "1": 
                statusInp = "working" 
            elif statusInp == "2": 
                statusInp = "needs service"
            elif statusInp == "3":
                statusInp = "out of order"
            try:
                status[int(inp) - 1][1] = statusInp
                print(f"{machines[int(inp) - 1][0]} now has the status ({status[int(inp) - 1][1]})")
            except:
                print("index not found")
            input("\n press enter to continue")
        case "5":
            inp = input("enter catagory $ ")
            print("")
            for i,v in enumerate(machines):          
                if categories[i] == inp:
                    print(f"{i + 1}. {v} <{status[i]}>")
            input("\n press enter to continue")
        case "6":
            for i,v in enumerate(machines):          
                if status[i] == "Needs Service":
                    print(f"{i + 1}. {v} ({categories[i]})")
            input("\n press enter to continue")
        case "7":
            exit()
