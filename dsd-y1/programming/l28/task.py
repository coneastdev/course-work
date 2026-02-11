import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

df = pd.read_csv("./dsd-y1/l28/students.csv")

def getInfo(df):
    print(df.head())
    print(df.info())
    print(df.describe())

# getInfo(df)

def task2(df: pd.DataFrame):
    print(f"length {len(df)}")
    print(f"mean: {df["Attendance"].mean()}")
    print(f"lowst: {df["Attendance"].min()}")
    print(f"highest: {df["Attendance"].max()}")

    print("")

    below = df[(df["Attendance"] < 80)]
    above = df[(df["Attendance"] >= 90)]

    print(f"students below 80% attendance: {len(below)}")
    print(f"students at or above 90% attendance: {len(above)}")

    print(df["Grade"].value_counts().sort_index())

# task2(df)

def task3(df: pd.DataFrame):
    at_risk = (df["Attendance"] < 80)

    df.insert(3, "AtRisk", at_risk)

    return df

#df = task3(df)
#print(df.head())

def task4(df: pd.DataFrame):
    df = df.sort_values("Attendance", ascending=False)

    print(df.head())

# task4(df)

def task5(df: pd.DataFrame):
    # hist
    fig, ax = plt.subplots()
    ax.hist(df["Attendance"], bins=6)
    ax.set_xlabel("Attendance %")
    ax.set_ylabel("Frequency")

    # force y ticks to be integers
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))

    plt.show()

task5(df)