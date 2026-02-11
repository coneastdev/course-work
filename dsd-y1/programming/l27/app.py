import pandas as pd
import kagglehub
import matplotlib.pyplot as plt
import numpy as np
import re

PATH = kagglehub.dataset_download("datadrivendecision/trump-tweets-2009-2025")

print("Path to dataset files:", PATH)

df = pd.read_csv(PATH + "/djt_posts_dec2025.csv")


# def tokenize(x):
#     if pd.isna(x):
#         return []
#     if isinstance(x, str):
#         return re.findall(r"\w+", x)
#     return [] 

def getWordUsageOfDT(df, mode):
    # words = df["text"].apply(tokenize).explode().dropna().reset_index(drop=True)

    words = (
        df["text"]
        .fillna("")                        # remove NaN
        .astype(str)
        .str.findall(r"\w+")               # returns list of tokens per row
        .explode()                         # safe because every row has a list
        .str.lower()
        .replace("", np.nan)
        .dropna()
        .reset_index(drop=True)
    )

    freq = words.value_counts()

    top = freq

    if mode == "pie":
        top_n = 1000
        top = freq.nlargest(top_n)
    elif mode == "find":
        top = freq

    sizes = top.values.astype(float)   # numeric sizes
    labels = top.index.tolist()        # labels (strings)

    if mode == "pie"
        plt.figure(figsize=(7,7))
        plt.pie(sizes,
                labels=labels,            # <- use labels=, not positional
                autopct='%1.1f%%',
                startangle=90)
        plt.axis('equal')                  # keep the pie circular
        plt.title(f'Top {len(labels)} words')
        plt.show()

    if mode == "find":
        word = "america"

        wordIndex = labels.index(word)

        print(f"{word} apeared: {sizes[wordIndex]} times")

if __name__ == "__main__":
    getWordUsageOfDT(df, "pie")
