arcade = {
    "Piball wizzerd": {
        "catagory": ["Pinball", "Mechanical"],
        "status": "Working"
    },
    "Retro racer": {
        "catagory": ["Racing", "Digital"],
        "status": "Needs Service"
    }
}

while True:
    print("###### arcade dictionary #####")
    print("1.View Machines\n2.Add machine\n3.Update machine status\n4.Remove machine\m5.Exit")
    select = input("Enter selection number $ ")
    match select:
        case "1":
            print("")
            for machine in arcade:
                print(f"{machine} ({", ".join(arcade[machine]["catagory"])}) [{arcade[machine]["status"]}]")
            input("\nPress enter to continue $ ")
        case "2":
            name = input("Enter machine name $ ")
            status = ""

            print("\nSelect status\n1.Working\n2.Needs Service\n3.Out Of Order")
            match input("Input selection number $ "):
                case "1":
                    status = "Working"
                case "2":
                    status = "Needs Service"
                case "3":
                    status = "Out Of Service"

            catagory = []

            while True:
                cat = input("Enter catagory $ ")
                catagory.append(cat)
                if input("Add another? Y/n $ ").lower() != "y":
                    break
            try:
                arcade[name] = {
                    "catagory": catagory,
                    "status": status
                }
                print(f"Added {name} ({", ".join(arcade[name]["catagory"])}) [{arcade[name]["status"]}]")
                input("\nPress enter to continue $ ")
            except:
                if arcade[name] != None:
                    print("Machine already exists")
                else:
                    print("Invalid input")
        case "3":
            print("")
            name = input("Enter machine name $ ")
            if arcade[name] == None:
                print("machine not found")
            else:
                status = ""
                print("\nSelect status\n1.Working\n2.Needs Service\n3.Out Of Order")
                match input("Input selection number $ "):
                    case "1":
                        status = "Working"
                    case "2":
                        status = "Needs Service"
                    case "3":
                        status = "Out Of Service"
                
                arcade[name]["status"] = status

                print(f"Changed the status of {name} to {arcade[name]["status"]}")
                input("\nPress enter to continue $ ")
        case "4":
            print("")
            name = input("Enter machine name $ ")
            if arcade[name] == None:
                print("machine not found")
            else:
                
                arcade.pop(name)

                print(f"Removed {name}")
                input("\nPress enter to continue $ ")
        case "5":
            quit()