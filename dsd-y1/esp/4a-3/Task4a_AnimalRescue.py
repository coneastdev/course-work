import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# functions

def get_total_by_time(df: pd.DataFrame, type: str) -> pd.DataFrame:
    """
    Creates a pandas series of interactions based on time of day.
    Args:
        df (DataFrame): DataFrame containing time, type, likes, shares and comments.
        type (str): The topic type you want sorted by.
    """
    df = df[df["Post Type"] == type]
    df = df.groupby("Time")[["Likes", "Shares", "Comments"]].sum()
    df["Total"] = df["Comments"] + df["Shares"] + df["Likes"]
    df = df.sort_index()
    
    return df

# graphs

# Plot average statistics
def show_average_stats(df: pd.DataFrame):
    """
    Will output a plot graph of average daily likes, shares and comments from 'task4.csv'.
    Args:
        df (DataFrame): DataFrame containing likes, shares and comments.
    """
    df = pd.read_csv("Task4a_data.csv")
    
    # plot likes
    likes = df["Likes"]
    plt.plot(likes.index, likes, linewidth=3)
    
    # plot shares
    shares = df["Shares"]
    plt.plot(shares.index, shares, linewidth=3)
    
    # plot comments
    comments = df["Comments"]
    plt.plot(comments.index, comments, linewidth=3)
    
    # configure plot
    plt.xlabel("Days")
    plt.ylabel("Likes, Shares & Comments")
    plt.title("Average Statistics By Day")
    
    plt.xticks(range(60))
    
    plt.grid(True)
    plt.legend(["Likes", "Shares", "Comments"], loc="upper right", title="Interaction Types")
    
    plt.show()
    
# bar chart type by interactions
def show_average_interactions_by_topic(df: pd.DataFrame):
    """
    Will output bar chart of post types sorted by interactions.
    Args:
        df (DataFrame): DataFrame containing type, likes, shares and comments.
    """
    topics_by_interaction = df.groupby(["Post Type"])[["Likes", "Shares", "Comments"]].sum()
    topics_by_interaction["Avg"] = (topics_by_interaction["Comments"] + topics_by_interaction["Shares"] + topics_by_interaction["Likes"]) / 3
    topics_by_interaction = topics_by_interaction.sort_values(by="Avg", ascending=False)
    
    # set bar chart widths
    w, x = 0.35, np.arange(len(topics_by_interaction.index))
    
    # bar chart values
    plt.bar(x - w/2, topics_by_interaction["Likes"], width=w, label="Likes")
    plt.bar(x, topics_by_interaction["Shares"], width=w, label="Shares")
    plt.bar(x + w/2, topics_by_interaction["Comments"], width=w, label="Comments")
    plt.bar(x + w, topics_by_interaction["Avg"], width=w, label="Avg")
    
    # configure bar chart
    plt.xticks(x, topics_by_interaction.index)
    
    plt.xlabel("Post Type")
    plt.ylabel("Likes, Shares & Comments")
    plt.title("Average interactions By Topic")
    
    plt.grid(True)
    plt.legend(loc="upper right", title="Interaction Types")
    
    plt.show()
    
# plot interactions by time
def show_average_topic_interactions_by_time(df: pd.DataFrame):
    """
    Will output bar chart of topic interactions interactions by times
    Args:
        df (DataFrame): DataFrame containing time, type, likes, shares and comments.
    """
    # time ranges for x ticks and reindex
    time_order = [
        "06:00 - 08:00", "08:01 - 10:00", "10:01 - 12:00",
        "12:01 - 14:00", "14:01 - 16:00", "16:01 - 18:00",
        "18:01 - 20:00", "20:01 - 22:00", "22:01 - 00:00"
    ]
    
    # make time categorical so it sorts in chart
    df["Time"] = pd.Categorical(df["Time"], categories=time_order, ordered=True)
    
    # Advertisements
    advertisements = get_total_by_time(df, "Advertisement").reindex(time_order).fillna(0)
    plt.plot(advertisements.index, advertisements["Total"], label="Advertisements", linewidth=3)
    
    # Images
    images = get_total_by_time(df, "Image").reindex(time_order).fillna(0)
    plt.plot(images.index, images["Total"], label="Image", linewidth=3)
    
    # News/Updates
    news_or_updates = get_total_by_time(df, "News/update").reindex(time_order).fillna(0)
    plt.plot(news_or_updates.index, news_or_updates["Total"], label="News/update", linewidth=3)
    
    # Polls
    polls = get_total_by_time(df, "Poll").reindex(time_order).fillna(0)
    plt.plot(polls.index, polls["Total"], label="Poll", linewidth=3)

    # Avg
    avg = (advertisements["Total"] + images["Total"] + news_or_updates["Total"] + polls["Total"]) / 4
    plt.plot(polls.index, avg, label="Avg", linewidth=3)

    # Configure plot
    plt.xlabel("Time")
    plt.ylabel("Total Interaction")
    plt.title("Topic Interactions By Time")
    
    plt.xticks(time_order)
    plt.grid()
    
    plt.legend()
    plt.show()
    
    
# starting function, will loop endlessly till quit
def main_menu(df=None):
    flag = True

    while flag:

        print("#################################################")
        print("############## Snowy Animal Rescue ##############")
        print("#################################################")
        print("")
        print("########### Please select an option #############")
        print("### 1. Average Social Media Interaction Data")
        print("### 2. Post Type Interaction")
        print("### 3. Post Type Interaction By Time")
        print("### 4. Quit Application")

        choice = input('Enter your number selection here: ')

        try:
            int(choice)
        except:
            print("Invalid Number Submitted")
            flag = True
        else:    
            if choice in ["1", "2", "3", "4"]:
                print('Option Selected')
                flag = False
            else:
                print("Nonexistent Option Selected")
                flag = True
    
    # loads df here so main menu is not slow to load
    if df is None:
        print("Loading Data...")
        df: pd.DataFrame = pd.read_csv("Task4a_data.csv")
    
    if choice == "1":
        show_average_stats(df)
    elif choice == "2":
        show_average_interactions_by_topic(df)
    elif choice == "3":
        show_average_topic_interactions_by_time(df)
    elif choice == "4":
        quit()
        
    main_menu(df)
            
if __name__ == "__main__":
    main_menu()
    