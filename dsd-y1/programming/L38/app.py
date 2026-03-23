import string
import os
import pandas as pd
import numpy as np

map = pd.read_excel("./dsd-y1/programming/l38/map.xlsx", header=None)

columns = list(string.ascii_uppercase[:len(map.columns)])

map.columns = columns
map.index = np.arange(1, len(map) + 1)

current_map = map
map_data = {"plr": ["B", "2"], "exit": ["F", "10"]}

def load_maze(level: int):
    map = pd.read_excel("./dsd-y1/programming/l38/map.xlsx", header=None)

    columns = list(string.ascii_uppercase[:len(map.columns)])
    map.columns = columns
    map.index = np.arange(1, len(map) + 1)

    current_map = map
    map_data = {"plr": ["B", "2"], "exit": ["F", "10"]}

    plr_pos = ["A", "1"]

    for col in current_map.columns:
        pos = col.iloc("p")
        


    # map_data["plr"] = current_map.loc()

def display_maze():
    os.system("cls")
    print(current_map)

def move_player(direction):
    return

def check_win():
    return

def game():
    plrMovement = input("Enter direction to move $ ").lower()
    match plrMovement:
        case "n":
            print()
    game()

def main():
    print("##### py maze crawler #####")
    print("1. new run")
    print("2. load floor")
    print("3. quit")

    selection = input("Enter selection number $ ")
    if selection == "1":
        game()
    main()

if __name__ == "__main__":
    main()