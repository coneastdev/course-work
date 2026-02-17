import math
import random
from functools import cache

import numpy as np
import matplotlib as plt
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("joebeachcapital/30000-spotify-songs")

# settings
QUESTIONS = 5


@cache
def start():
    print("##### Welcom To The Grand Spotify Quiz #####")
    print("loading data...")

    df = pd.read_csv(path + "/spotify_songs.csv")

    genres = df["playlist_genre"].unique()
    artists = df["track_artist"].unique()
    albumns = df["track_album_name"].unique()

    popular = df[df["track_popularity"] > 75].sort_values(by="track_popularity", ascending=False)
    unpopular = df[df["track_popularity"] < 25].sort_values(by="track_popularity", ascending=True)

    results = []
    catagories = np.array(["genres", "artists", "albumns", "popular", "unpopular"])

    while len(results) < QUESTIONS:
        catagorey = np.random.choice(catagories)

        if catagorey == "genres":
            corect = np.random.choice(genres)
            
            songs = df[df["playlist_genre"] == corect]

            song = songs.sample(1)

            print(f"What genre is the song {song["track_name"]} by {song["track_artist"]}?")

            for index, gen in enumerate(genres):
                print(f"{index + 1}. {gen}")
            userInput = input("EEnter number $ ")
            if userInput == corect:
                print("Corect!")
            else:
                print("Wrong!")
            break
            



start()