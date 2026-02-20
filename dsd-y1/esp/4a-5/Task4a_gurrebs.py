import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Displays the main menu and collects choice of menu item

def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show total sales for a specific item") 
        print("2. Show Menu Item with highst Total And Average Sales")

        main_menu_choice = input("Please enter the number of your choice (1-2): ")

        try:
            int(main_menu_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 2:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

#Menu item selection form user and validates it
def get_product_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a menu item form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Nachos")
        print("2.  Soup")
        print("3.  Burger")
        print("4.  Brisket")
        print("5.  Ribs")
        print("6.  Corn")
        print("7.  Fries")
        print("8.  Salad")
        print("######################################################")

        menu_list = ["Nachos","Soup","Burger", "Brisket","Ribs","Corn", "Fries", "Salad"]

        item_choice = input("Please enter the number of your choice (1-8): ")

        try:
            int(item_choice)
        except:
            print("Sorry, you did not enter a valid choice")
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 8:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name

#Gets user input of start of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_start_date():
    
    flag = True
    
    while flag:
        start_date = input('Please enter start date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(start_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return start_date

#Gets user input of end of date range
#Converts to a date to check data entry is in correct format and then returns it as a string
def get_end_date():
    
    flag = True
    
    while flag:
        end_date = input('Please enter end date for your time range (DD/MM/YYYY) : ')

        try:
           pd.to_datetime(end_date, dayfirst=True)
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return end_date


#imports data set and extracts data and returns data for a specific menu item within a user defined range
def get_selected_item(startdate, enddate) -> pd.DataFrame:
    df = pd.read_csv("./dsd-y1/esp/4a-5/Task4a_data.csv") 
    df2 = df.loc[:,startdate:enddate]
    df2["Menu Item"] = df["Menu Item"]
    return df2

def get_weekly_value(df: pd.Series):
    weeklyRevenue = []
    weekIndex = []

    dayCounter = 0
    thisWeeksRevenue = 0

    for day in df:
        dayCounter += 1
        thisWeeksRevenue += day
        if dayCounter == 7:
            weeklyRevenue.append(thisWeeksRevenue)
            weekIndex.append(len(weekIndex) + 1)
            dayCounter = 0
            thisWeeksRevenue = 0

    return [weeklyRevenue, weekIndex]
     
main_menu = menu()
if main_menu == 1:

    item = get_product_choice()

    df = pd.read_csv("./dsd-y1/esp/4a-5/Task4a_data.csv")
    df = df[df["Menu Item"] == item]

    lunch = df[df["Service"] == "Lunch"]
    lunch = df[lunch.columns[3:]].reset_index()

    dinner = df[df["Service"] == "Dinner"]
    dinner = df[dinner.columns[3:]].reset_index()

    weeklyLunch = get_weekly_value(lunch.loc[0])
    weeklyDinner = get_weekly_value(dinner.loc[1])

    total = (np.array(weeklyLunch[0]) + np.array(weeklyDinner[0]))

    print(weeklyLunch)

    plt.plot(weeklyLunch[1], weeklyLunch[0], label="Lunch")
    plt.plot(weeklyDinner[1], weeklyDinner[0], label="Dinner")
    plt.plot(weeklyLunch[1], total, label="Total")

    plt.xlabel("Weekly sum")
    plt.ylabel("Money £")
    plt.xticks(weeklyLunch[1])
    plt.title(f"Weekly Sales Revenue Of {item}")

    plt.grid(True)
    plt.legend()

    plt.show()
elif main_menu == 2:
    start_date = get_start_date()
    end_date = get_end_date()
 
    df = get_selected_item(start_date, end_date)

    df = df.groupby("Menu Item").sum()
    df = df.iloc[0:-2].reindex()

    sums = []
    avg = []

    for index in df.index:
        sums.append(sum(df.loc[index]))
        avg.append(np.mean(df.loc[index]))

    plt.bar(df.index + " sum", sums)
    plt.bar(df.index + " avg", avg)
    
    plt.yticks(np.array(range((np.array(sums).max() // 25) + 5)) * 25)
    plt.title(f"Total & Average Sales between {start_date} and {end_date}")
    
    plt.grid(True)
    plt.xlabel("Menu Items")
    plt.ylabel("Total/Avg Revenue")

    plt.show()
