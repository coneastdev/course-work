import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PATH_TO_XLSX = ".\dsd-y1\misc\matplotlib\driving-licence-data-feb-2026.xlsx"

def show_licence_holders_by_age():
    age_range_labels = ["15-25", "26-36", "37-47", "48-58", "59-69", "70-80", "81-92", "93-103", "104-114"]
    age_range_bins = [15, 26, 37, 48, 59, 70, 81, 93, 104, 115]

    df = pd.read_excel(PATH_TO_XLSX, "DRL0101- February 2026")

    df["age_group"] = pd.cut(df["Age"], bins=age_range_bins, labels=age_range_labels, right=False)
    df = df.groupby('age_group', observed=False).sum().round()

    w, x = 0.4, np.arange(len(age_range_labels))
    fig, ax = plt.subplots()

    subplot_y_ticks = range(10) * (df["Full - Total"].max() // 10)
    subplot_y_labels = np.array(range(10) * (df["Full - Total"].max() // 10)).astype(str)

    ax.bar(x - w/2, df["Provisional Licences - Male"], width=w, label="Provisional Male")
    ax.bar(x - w, df["Provisional Licences - Female"], width=w, label="Provisional Female")
    ax.bar(x + w/2, df["Full Licences - Male"], width=w, label="Full Licence Male")
    ax.bar(x + w, df["Full Licences - Female"], width=w, label="Full Licence Female")

    plt.setp(ax, yticks=subplot_y_ticks, yticklabels=subplot_y_labels)
    ax.set_xticklabels(age_range_labels)
    fig.legend()

    ax.set_xlabel("Age ranges")
    ax.set_ylabel("Total Licence Holders")

    plt.show()

def main():
    print("##### bar charts.py #####")
    print("1. licence holders by age ranges")

    selection = input("enter selection number $ ")
    match (selection):
        case "1":
            show_licence_holders_by_age()

main()