import datetime
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./dsd-y1/esp/4a-4/Task_4a.csv')

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

    # to get the amomount of months in csv
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

def show_region_sizes(region):
    properties = df[df["Region"] == region]

    # average sizes by reigon
    sizes = properties.groupby("Property Type")["Rooms"].mean()

    plt.bar(sizes.index, sizes)

    plt.xlabel("Protperty Types")
    plt.ylabel("Avg Rooms")
    plt.title(f"Avg Rooms By Property Type in {region}")

    plt.show()

def show_top_region_sizes():
    avg_sizes = df.groupby("Region")["Rooms"].mean().sort_values(ascending=False)

    plt.bar(avg_sizes.index, avg_sizes)

    plt.xlabel("Protperty Types")
    plt.ylabel("Avg Rooms")
    plt.title("Property Size By Region")

    plt.show()

def show_regions():
    values = df.groupby("Region")[df.columns[4:45]].mean()
    
    values['Average'] = values.mean(axis=1)
    values = values.sort_values(by="Average", ascending=False)

    plt.bar(values.index, values["Average"])

    plt.xlabel("Regions")
    plt.ylabel("Avg Value")
    plt.title("Average Value Of Protperty By Region")

    plt.show()

def main_menu():
    print("\t\t****Newhaven Property Analysis Program****")
    print("1) Show region trends")
    print("2) Show region property sizes")
    print("3) Show top region property sizes")
    print("4) Show top regions")
    
    user_input = input("Enter option number or name $ ")

    if user_input == "1":
        region = select_region()
        show_region_trends(region)
    elif user_input == "2":
        region = select_region()
        show_region_sizes(region)
    elif user_input == "3":
        show_top_region_sizes()
    elif user_input == "4":
        show_regions()
    else:
        return "Input is out of range"
    
    main_menu()
    
if __name__ == "__main__":
    main_menu()
