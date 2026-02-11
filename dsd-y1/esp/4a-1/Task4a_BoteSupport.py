import pandas as pd
import csv
import matplotlib.pyplot as plt

# Outputs the initial menu and validates the input
def main_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############# Botes Parcels CRM System #############")
        print("####################################################")
        print("")
        print("########### Please select an option ################")
        print("### 1. Total issues by type")
        print("### 2. Issues and resoloutions by region")
        print("### 3. Quit")

        choice = input('Enter your number selection here: ')

        validChoices = ["1", "2", "3"]

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid number")
            flag = True
        else:  
            # check that its one of the valid options, using a list fo readability
            if choice in validChoices: 
                print('Choice accepted!')
                flag = False
            else:
                print("Sorry, you did not enter a valid option")

    return choice

# Submenu for totals, provides type check validation for the input and returns issue type as a string
def total_menu():
    flag = True

    while flag:

        print("####################################################")
        print("############## Total issues by type ################")
        print("####################################################")
        print("")
        print("########## Please select an issue type ##########")
        print("### 1. Customer Account Issue")   
        print("### 2. Delivery Issue") 
        print("### 3. Collection Issue")  
        print("### 4. Service Complaint")

        choice = input('Enter your number selection here: ')

        validChoices = ["1", "2", "3", "4"]

        try:
            int(choice)
        except:
            print("Sorry, you did not enter a valid number")
            flag = True
        else:    
            # check that its one of the valid options, using a list fo readability
            if choice in validChoices:
                print('Choice accepted!')
                choice = int(choice)
                flag = False
            else:
                print("Sorry, you did not enter a valid option")

    issueTypeList = ["Customer Account Issue", "Delivery Issue", "Collection Issue", "Service Complaint"]
    

    issueType = issueTypeList[choice - 1]
  
    return issueType

# Creates a new dataframe then counts the number of occurences of the requested issue type
def get_total_data(total_menu_choice):
    df = pd.read_csv("Task4a_data.csv")
    
    total = df['Issue Type'].value_counts()[total_menu_choice]

    issueData = df[df["Issue Type"] == total_menu_choice]

    averageTimeTaken = issueData["Days To Resolve"].mean()

    msg = f"The total number of issues logged as a {total_menu_choice} was: {total} and the average time is: {averageTimeTaken.round(1)} days"
    
    return msg

def show_issues_by_reigon(region):
    df = pd.read_csv("Task4a_data.csv")

    regionDf = df[df["Region"] == region]

    issues = regionDf["Issue Type"].value_counts()
    resoloutions = regionDf["How Resolved"].value_counts()

    print(issues)

    fig, ax = plt.subplots()

    size = 0.3

    tab20c = plt.color_sequences["tab20c"]
    outer_colors = [tab20c[i] for i in [0, 4, 8]]
    inner_colors = [tab20c[i] for i in [1, 2, 5, 6, 9, 10]]

    ax.pie(issues, radius=1, colors=outer_colors,
       wedgeprops=dict(width=size, edgecolor='w'), labels=issues.index)
    ax.pie(resoloutions, radius=1-size, colors=inner_colors,
       wedgeprops=dict(width=size, edgecolor='w'), labels=resoloutions.index)
    
    ax.legend(loc="best")

    plt.show()

def menu_selector(menu="main"):
    print("")
    if menu == "main":
        main_menu_choice = main_menu()

        # Total issues by type
        if main_menu_choice ==  "1":
            menu_selector("total")

        if main_menu_choice == "2":
            menu_selector("reigon")

        # Quit
        elif main_menu_choice == "3":
            quit()
    
    if menu == "total":
        total_menu_choice = total_menu()
        print(get_total_data(total_menu_choice))

        if input("Select another issue? Y/n").lower() in ["y", "ye", "yes"]:
            menu_selector("total")
    
    if menu == "reigon":
        show_issues_by_reigon("London")

    menu_selector("main")

# Check its main encase unit tests are writen in the future
if __name__ == "__main__":
    menu_selector()

