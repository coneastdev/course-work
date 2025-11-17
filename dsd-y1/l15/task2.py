films = {
    "Wonka": {
        "Time": {
            "Start": "17:45",
            "End": "19:00",
            "Duration": "1:15"
        },
        "room": {
            "Wing": "West",
            "Number": 2,
            "Side" : "Left",

            "Seats": {
                "Amount": 40,
                "Reserved": 15,
                "Left": 25
            }
        }
    },
    "Dune 2": {
        "Time": {
            "Start": "20:15",
            "End": "22:30",
            "Duration": "2:15"
        },
        "room": {
            "Wing": "East",
            "Number": 6,
            "Side" : "Right",

            "Seats": {
                "Amount": 35,
                "Reserved": 25,
                "Left": 10
            }
        }
    }
}

while True:
    print("##### film view #####")
    print("1.view films\n2.book film\n3.add film\n4.remove film\n5.exit")
    match input("Select option number $ "):
        case "1":
            for filmName in films:
                film = films[filmName]
                print({filmName})