import os

analytics = {
    "customers": 0,
    "revenue": 0,
    "lanes": {
        "used": 0,
        "left": 20
    },
    "needsRestock": []
}

menu = {
    "drinks": {
        "soda": {
            "stock": 32,
            "price": 299 # pennys
        },
        "cider": {
            "stock": 11,
            "price": 499
        },
        "juice": {
            "stock": 26,
            "price": 299
        }
    },
    "food": {
        "chips": {
            "stock": 62,
            "price": 399
        },
        "pizza": {
            "stock": 11,
            "price": 499
        },
        "nachos": {
            "stock": 36,
            "price": 399
        }
    }
}

laneInfo = {
    "maxPlayers": 6,
    "lanes": 20,
    "maxRounds": 5,
    "vipLanes": [19, 20]
}

# "1": {
#     "ocupied": True,
#     "vip": False,
#     "people": 1,
#     "roundsLeft": 0,
#     "round": 0,
#     "players": {
#         "john doe": {
#             "score": [[3,1], [9,1], [0, 0]],
#             "bumpers": False
#         }
#     }
# }

lanes = {}

for i in range(1, laneInfo["lanes"] + 1):
    lanes[str(i)] = {
        "ocupied": False,
        "vip": True if i in laneInfo["vipLanes"] else False,
        "people": 0,
        "roundsLeft": 0,
        "round": 0,
        "players": {}
    }

pricing = {
    "elderly": 599, # pennys
    "adult": 899,
    "child": 499
}

offers = {
    "mealDeal": {
        "enabled": True,
        "savings": 10 # percentage
    },
    "disabledWithCarer": {
        "enabled": True,
        "savings": 100 # saving only for the carer the disabled person still needs to be paid for
    },
    "extraGameReduction": {
        "enabled": True,
        "savings": 25
    }
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# menu options

def analytics():
    print(f"""###### analytics ######
customers today: {analytics['customers']}
revenue today: £{analytics['revenue']/100:.2f}
lanes used: {analytics['lanes']['used']}
lanes left: {analytics['lanes']['left']}
needs restock: {', '.join(analytics['needsRestock']) if len(analytics['needsRestock']) > 0 else 'none'}
          """)
    input("press enter to go back ")

def laneManager():
    print("###### lane manager ######")
    pairs = []
    for lane in lanes:
        status = "ocupied" if lanes[lane]["ocupied"] else "free"
        vip = " (VIP)" if lanes[lane]["vip"] else ""
        pairs.append(f"lane {lane}{vip}: {status}")
    for i in range(0, len(pairs), 4):
        try:
            print(f"{pairs[i]:<25}{pairs[i+1]:<25}{pairs[i+2]:<25}{pairs[i+3]}")
        except IndexError:
            print(f"{pairs[i]}")
    selection = input("enter lane number to manage or press enter to go back $ ")
    clear()
    if selection in lanes:
        lane = lanes[selection]
        print(f"""###### managing lane {selection} ######
status: {"ocupied" if lane["ocupied"] else "free"}
vip: {"yes" if lane["vip"] else "no"}
people: {lane["people"]}
rounds left: {lane["roundsLeft"]}, round: {lane["round"]}
players:""")
        for player in lane["players"]:
            info = lane["players"][player]
            print(f"- {player}: score: {info['score']}, bumpers: {'yes' if info['bumpers'] else 'no'}")
        print(f"1.{"book lane" if not lane['ocupied'] else "free lane"} 2.alter players 3.alter rounds")
        selection = input("Enter option number $ ")
    elif selection == "":
        return
    else:
        print(f"{selection} is an invalid input, try again")
        input("press enter to continue ")

def foodAndDrinks():
    print(f"""###### food and drinks ######

    """)
    input("press enter to go back ")

def foodAndDrinks():
    print(f"""###### food and drinks ######

    """)
    input("press enter to go back ")

def arcadeManager():
    print(f"""###### arcade manager ######

    """)
    input("press enter to go back ")

# main menu

def home():
    clear()
    print("""###### bowl a tron 9000 ######

1.analytics
2.lanes
3.food and drinks
4.arcade service
          """)
    selection = input("Enter selection number $ ")
    clear()
    match selection:
        case "1":
            analytics()
        case "2":
            laneManager()
        case "3":
            foodAndDrinks()
        case "4":
            print("unfinshed")
            input("press enter to continue ")
        case _:
            print(f"{selection} is an invalid input, try again")
            input("press enter to continue ")
    home()

if __name__ == "__main__":
    home()