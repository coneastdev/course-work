import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PATH_TO_XLSX = ".\dsd-y1\misc\matplotlib\driving-licence-data-feb-2026.xlsx"

def show_licence_holders_by_age():
    age_range_labels = ["0-14", "15-25", "26-36", "37-47", "48-58", "59-69", "70-80", "81-92", "93-103", "104-114"]
    age_range_bins = [0, 15, 26, 37, 48, 59, 70, 81, 93, 104, 115]

    df = pd.read_excel(PATH_TO_XLSX, "DRL0101- February 2026")

    df["age_group"] = pd.cut(df["Age"], bins=age_range_bins, labels=age_range_labels, right=False)
    df = df.groupby('age_group', observed=False).sum().round()

    fig, ax = plt.subplots()

    ax.boxplot([df["Provisional Licences - Male"], df["Provisional Licences - Female"], df["Full Licences - Male"], df["Full Licences - Female"]])

    plt.setp(ax, yticklabels=age_range_labels)
    ax.set_xticklabels(["Provisional Licences - Male", "Provisional Licences - Female", "Full Licences - Male", "Full Licences - Female"])
    #fig.legend()

    ax.set_xlabel("Age ranges")
    ax.set_ylabel("Total Licence Holders")

    plt.show()

def main():
    print("##### bar charts.py #####")
    print("1. licence holders by age ranges (box chart)")

    selection = input("enter selection number $ ")
    match (selection):
        case "1":
            show_licence_holders_by_age()

main()