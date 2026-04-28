import os
import random

invetory: list[str] = []
current_location: str = ""

def cls():
    os.system("cls")

def move_to(location: str):
    cls()
    match(location):
        case "intro":
            current_location = "intro"
            print(
                """
                A secluded clearing where you awoke, there is nothing here.

                Before you are two paths, to the 'East' is a lightly troden forest path,
                the 'West' is a river crossing.
                """)
            
            while True:
                direction = input("Enter the direction you want to go $ ")
                if direction.lower() in ["e", "east"]:
                    move_to("path")
                elif direction.lower() in ["w", "west"]:
                    move_to("river")
                else:
                    print(f"{direction} is not a valid direction.")
        
        case "path":
            current_location = "path"

            print(f"You {"stroll" if random.randint(1, 2) == 1 else "stride"} down the worn path,\nyou cannot see an end in sight, however its too late to turn back now.")

            if random.randint(1, 10) == 10:
                print("FLASH, a deer sprints pass you, heading into the forest. You have two options, continue going 'East' down the path, or follow the dear 'North'")
                while True:
                    direction = input("Enter the direction you want to go $ ")
                    if direction.lower() in ["e", "east"]:
                        move_to("path")
                    elif direction.lower() in ["w", "west"]:
                        move_to("river")
                    else:
                        print(f"{direction} is not a valid direction.")
            elif random.randint(1, 8) == 8:
                print("Out of the corner of your eye you see an end, a rickity country house at the end of the path. Do you go 'East' to the house, or 'West' back to the clearing.")
            else:
                print("you only have one option, 'East'")

        case _:
            print(f"{location} is an invalid location, going back to last location.")
            move_to(current_location)

def intro():
    print("##### py adventure #####\n")

    print(
        """
        You awake in a forest celaring, tall trees looming over you.
        With nomemory of how you got here, only one option remains.
        Explore and find a way to contact others to help you.
        """)
    
    input("Press enter to continue $ ")

    move_to("intro")
