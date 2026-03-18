import string
import os
import pandas as pd
import numpy as np

map = pd.read_excel("./dsd-y1/programming/l38/map.xlsx", header=None)

COLUMNS = list(string.ascii_uppercase[:len(map.columns)])

map.columns = COLUMNS
map.index = np.arange(1, len(map) + 1)

current_map = map

def display_maze():
    os.system("cls")
    print(current_map)

def move_player(direction):
    return

def check_win():
    return

def game():
    plrMovement = input("Enter direction to move $ ")
    game()

def main():
    print("##### py maze crawler #####")
    print("1. new run")
    print("2. load floor")
    print("3. quit")

    selection = input("Enter selection number $ ")
    main()

print(map)