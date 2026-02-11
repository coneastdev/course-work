# games = [
#     ["half life alyx", ""],
#     ["tf2", "played"],
#     ["minecraft", "favorite"]
# ]

games = []

while True:
    print("----- game-a-tron-9.9000 -----\n1. view games\n2. add game\n3. remove game\n4. change game status\n5. exit")
    inp = input("select option $ ")
    print("")
    match inp:
        case "1":
            for i,v in enumerate(games):
                if v[1] != "":
                    print(f"{i + 1}. {v[0]} ( {v[1]} )")
                else:
                    print(f"{i + 1}. {v[0]}")
            input("\n press enter to continue")
        case "2":
            games.append([input("enter game name $ "), ""])
            print(f"{games[-1][0]} added to games")
            input("\n press enter to continue")
        case "3":
            for i,v in enumerate(games):
                if v[1] != "":
                    print(f"{i + 1}. {v[0]} ( {v[1]} )")
                else:
                    print(f"{i + 1}. {v[0]}")
            inp = input("enter index $ ")
            try:
                games.pop(int(inp) - 1)
            except:
                print("index not found")
            input("\n press enter to continue")
        case "4":
            for i,v in enumerate(games):
                if v[1] != "":
                    print(f"{i + 1}. {v[0]} ( {v[1]} )")
                else:
                    print(f"{i + 1}. {v[0]}")
            inp = input("enter index $ ")
            statusInp = input("enter status $ ")
            try:
                games[int(inp) - 1][1] = statusInp
                print(f"{games[int(inp) - 1][0]} now has the status {games[int(inp) - 1][1]}")
            except:
                print("index not found")
            input("\n press enter to continue")
        case "5":
            exit()
