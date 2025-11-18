import os

analytics = {
    "customers": 0,
    "revenue": 0,
    "lanes": {
        "used": 0,
        "left": 20
    }
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

lanes = {
    "1": {
        "ocupied": False,
        "people": 0,
        "roundsLeft": 0,
        "level": 0,
        "players": {
            "john doe": {
                "score": [[3,1], [9,1], [0, 0]],
                "bumpers": False
            }
        }
    }
}

pricing = {
    "adult": 899, # pennys
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

def analytics():
    print("unfinshed")
    input("press enter to continue ")

def laneManager():
    print("unfinshed")
    input("press enter to continue ")

def foodAndDrinks():
    print("unfinshed")
    input("press enter to continue ")

def arcadeManager():
    print("unfinshed")
    input("press enter to continue ")


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
home()