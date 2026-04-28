import os
import platform
import random

inventory: list[str] = []
current_location: str = ""

def cls():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def move_to(location: str):
    cls()
    match(location):
        case "intro":
            current_location = location
            print(
    """
    A secluded clearing where you awoke, there is nothing here.

    Before you are two paths, to the 'East' is a lightly trodden forest path,
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
            current_location = location

            if random.randint(1, 2) == 1:
                print(
    """
    You stride down the lengthy path, 
    a sense of dread lingers, 
    but its too late to turn back now...
    """)
            else:
                print(
    """
    You stroll down the worn path, 
    you cannot see an end in sight, 
    however its too late to turn back now.
    """)

            rng = random.randint(1,100)
            if rng > 90:
                print(
    """
    FLASH, a deer sprints pass you, heading into the forest.
    You have two options, continue going 'East' down the path, or follow the dear 'North'
    """)
                while True:
                    direction = input("Enter the direction you want to go $ ")
                    if direction.lower() in ["e", "east"]:
                        move_to("path")
                    elif direction.lower() in ["n", "north"]:
                        move_to("woods")
                    else:
                        print(f"{direction} is not a valid direction.")
            elif rng > 70:
                print(
    """
    Out of the corner of your eye you see an new sight,
    a rickety, fallen-down country house at the end of the path.
    Do you go 'East' to the house, or 'West' back to the clearing.
    """)
                while True:
                    direction = input("Enter the direction you want to go $ ")
                    if direction.lower() in ["e", "east"]:
                        move_to("house")
                    elif direction.lower() in ["w", "west"]:
                        move_to("intro")
                    else:
                        print(f"{direction} is not a valid direction.")
            else:
                print("you only have one option, 'East'")
                while True:
                    direction = input("Enter the direction you want to go $ ")
                    if direction.lower() in ["e", "east"]:
                        move_to("path")
                    else:
                        print(f"{direction} is not a valid direction.")
        case "river":
            current_location = location
            print(
    """
    A peaceful stream, it wouldn't be too hard to cross,
    but a quaint hump bridge is slightly down stream.
    
    Do you go 'West', wading the stream, or go 'South', down stream to the bridge.
    """)
            while True:
                    direction = input("Enter the direction you want to go $ ")
                    if direction.lower() in ["w", "west"]:
                        move_to("house")
                    elif direction.lower() in ["s", "south"]:
                        move_to("intro")
                    else:
                        print(f"{direction} is not a valid direction.")

        case _:
            print(f"{location} is an invalid location, going back to last location.")
            move_to(current_location)

def intro():
    cls()
    print(
    """
    You awake in a forest clearing, tall trees looming over you.
    With no memory of how you got here, only one option remains.
    Explore and find a way to contact others to help you.
    """)
    
    input("Press enter to continue $ ")

    move_to("intro")

if __name__ == "__main__":
    intro()