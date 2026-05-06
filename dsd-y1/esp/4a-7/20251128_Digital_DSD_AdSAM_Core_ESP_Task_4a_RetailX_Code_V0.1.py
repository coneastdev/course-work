import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

CSV_PATH = "20251128_Digital_DSD_AdSAM_Core_ESP_Task_4a_RetailX_data_V0.1.csv"

#Generates submenu of available product codes and allows user to select a product to view
def get_product_id ():

    df = pd.read_csv(CSV_PATH)

    product_codes = df["Product ID"].unique().tolist()

    flag = True

    while flag:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("Select a product code:")
        for i in range(len(product_codes)):
            print(i+1, " ", product_codes[i])

        selection = input('Enter your number selection here: ')

        if selection.isdigit():
            selection = int(selection)
            flag = False
        else:
            flag = True

        
        product_ID = product_codes[selection -1]
   
    print("You have selected product id:",product_ID)
    return product_ID

#gets and converts user input from string to date format
def get_date(start_end):
    
    flag = True
    
    while flag:
        date = input('Please enter {} date for your date range (DD/MM/YYYY) : '.format(start_end))

        try:
           pd.to_datetime(date, format="%d/%m/%Y")
        except:
            print("Sorry, you did not enter a valid date")
            flag = True
        else:
            flag = False
    
    return date

#extracts data based on product ID within a user specified date range.
def get_data_by_ID_and_date(start_date, end_date):
    all_data = pd.read_csv(CSV_PATH)
    product_data = all_data

    product_data["Date"]= pd.to_datetime(product_data["Date"], format="%d/%m/%Y", errors="raise")
    
    date_range = (product_data["Date"] >= pd.to_datetime(start_date, format="%d/%m/%Y")) & \
                  (product_data["Date"] <= pd.to_datetime(end_date,format="%d/%m/%Y" ))
    
    extracted_data = product_data.loc[date_range]

    return extracted_data

#generates a total of the number of items sold for the extracted data
def calculate_total_sale (date_ID, product_id, start_date, end_date):
    total_sales = date_ID["Qty Sold"].sum()
    total_revenue = date_ID["Sales Price"].sum()

    print(f"\nThe total number of sales for product {product_id}, between {start_date} and {end_date} was: {total_sales}, and the total revnue was: £{round(total_revenue):,}")

def calculate_total_sales(date_ID: pd.DataFrame, start_date, end_date):
    total_sales = date_ID.groupby("Product ID")["Qty Sold"].sum()
    total_revenue = date_ID.groupby("Product ID")["Sales Price"].sum()

    plt.bar(total_sales.index, total_sales, width=0.5)
    plt.bar(total_sales.index, total_revenue, align="edge", width=0.5)

    plt.legend(["total sales", "total revenue"])
    plt.xlabel("products")
    plt.ylabel("Sales and revnue")
    plt.title(f"Sales & revenue of products from {start_date} - {end_date}")

    plt.show()

def calculate_total_sales_by_cat(date_ID: pd.DataFrame, start_date, end_date):
    total_sales = date_ID.groupby("Category")["Qty Sold"].sum()
    total_revenue = date_ID.groupby("Category")["Sales Price"].sum()

    plt.bar(total_sales.index, total_sales, width=0.5)
    plt.bar(total_sales.index, total_revenue, align="edge", width=0.5)

    plt.legend(["total sales", "total revenue"])
    plt.xlabel("Categories")
    plt.ylabel("Sales and revnue")
    plt.title(f"Sales & revenue of catagories from {start_date} - {end_date}")

    plt.show()

def calculate_sales_over_time(date_ID: pd.DataFrame, product_id, start_date, end_date):
    date_ID = date_ID[date_ID["Product ID"] == product_id]

    plt.plot(date_ID["Date"], date_ID["Qty Sold"])
    plt.plot(date_ID["Date"], date_ID["Sales Price"])

    plt.legend(["total sales", "total revenue"])
    plt.ylabel("Sales & revenue")
    plt.xlabel(f"Days from {start_date} to {end_date}")
    plt.title(f"Sales & revenue of {product_id} over time")

    plt.show()

def calculate_all_sales_over_time(date_ID: pd.DataFrame, start_date, end_date):
    plt.plot(date_ID["Date"], date_ID["Qty Sold"])
    plt.plot(date_ID["Date"], date_ID["Sales Price"])

    plt.legend(["total sales", "total revenue"])
    plt.ylabel("Sales & revenue")
    plt.xlabel(f"Days from {start_date} to {end_date}")
    plt.title(f"Sales & revenue over time")

    plt.show()

#Outputs the main menu and checks the user input
def main_menu():
    looping = True

    while looping:

        print("-"*66)
        print("---------- RetailX Sales Analysis Module ------------- ")
        print("-"*66)
        print("")
        print("--------------------- Main Menu --------------------- ")
        print("1. Total sales of single product")
        print("2. Total sales of all products")
        print("3. Total sales by catagories")
        print("4. Sales of single product over time")
        print("5. Total sales over time")
        print("6. Quit")

        choice = input("\nEnter your number selection here: ")

        if choice.isdigit() and choice in ["1", "2", "3", "4", "5", "6"]:
            looping = False
        else:
            print("Invalid selection")
            looping = True

    if choice == "1":
        product_id = get_product_id()
        start_date = get_date("start")
        end_date = get_date("end")
        date_ID = get_data_by_ID_and_date(start_date, end_date)
        calculate_total_sale(date_ID, product_id, start_date, end_date)
    elif choice == "2":
        start_date = get_date("start")
        end_date = get_date("end")
        date_ID = get_data_by_ID_and_date(start_date, end_date)
        calculate_total_sales(date_ID, start_date, end_date)
    elif choice == "3":
        start_date = get_date("start")
        end_date = get_date("end")
        date_ID = get_data_by_ID_and_date(start_date, end_date)
        calculate_total_sales_by_cat(date_ID, start_date, end_date)
    elif choice == "4":
        product_id = get_product_id()
        start_date = get_date("start")
        end_date = get_date("end")
        date_ID = get_data_by_ID_and_date(start_date, end_date)
        calculate_sales_over_time(date_ID, product_id, start_date, end_date)
    elif choice == "5":
        start_date = get_date("start")
        end_date = get_date("end")
        date_ID = get_data_by_ID_and_date(start_date, end_date)
        calculate_all_sales_over_time(date_ID, start_date, end_date)
    elif choice == "6":
        quit()
    main_menu()

main_menu()
