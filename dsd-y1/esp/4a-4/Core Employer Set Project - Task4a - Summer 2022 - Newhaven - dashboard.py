import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task_4a.csv')

def select_region() -> str:
    regions = df["Region"].unique()
    print("")
    for index, region in enumerate(regions):
        print(f"{index + 1}) {region}")

    while True:
        inp = input("Enter region number $ ")

        if inp.capitalize() in regions:
            return inp.capitalize()
        else:
            try:
                return regions[int(inp) - 1]
            except:
                print("Invalid country name or number")
    
def show_region_trends(region):
    properties = df[df["Region"] == region]

    width = len(df.columns) - 4

    for month in range((width)):
        if ((month * 11) + 5) > (width + 4):
            properties_year = properties.groupby("Region")[df.columns[ (month + 4) + (month * 11) : width + 4]].mean()
            plt.plot(properties_year.columns, properties_year.iloc[0,:])
        else:
            properties_year = properties.groupby("Region")[df.columns[ (month + 4) + (month * 11) : ((month + 4) + (month * 11)) + 13 ]].mean()
            plt.plot(properties_year.columns, properties_year.iloc[0,:])

    plt.xticks(rotation=45)
    plt.grid(True)

    plt.xlabel("Months & Years")
    plt.ylabel("Avg Value")

    plt.title(f"Avg House Prices In {region}")

    plt.show()

def main_menu():
    print("\t\t****Newhaven Property Analysis Program****")
    print("1) Show region trends")
    print("2) Show region property sizes")
    print("3) Show top regions")
    user_input = input("Enter option number or name $ ")

    if user_input == "1":
        region = select_region()
        show_region_trends(region)
    else:
        return "Input is out of range"
    
if __name__ == "__main__":
    main_menu()

# x = mainmenu()
# while x == 1 or x == 2:
#     if x == 1:
#         alldata()

#     elif x == 2:
#         while True:
#             print()

#             region = input("Please enter the name of the region you would like to check:")
#             region = region.capitalize()
#             if region in df.Region.values:
#                 while True:
#                     startdate = input("PLEASE ENTER A START DATE AS MONTH-YEAR e.g. JAN-20")
#                     startdate = startdate.capitalize()
#                     if startdate not in df.columns:
#                         print("Error start date not found")
#                     else:
#                         while True:
#                             enddate = input("PLEASE ENTER AN END DATE AS MONTH-YEAR e.g. JAN-20")
#                             enddate = enddate.capitalize()
#                             if enddate not in df.columns:
#                                 print("Error end date not found")
#                             else:
#                                 region_check(region, startdate, enddate)
#                                 break
#                         break
#                 break
#             else:
#                 print("Region not found")

#     x = mainmenu()
