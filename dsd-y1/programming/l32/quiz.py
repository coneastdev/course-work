import math
import random
from functools import cache
from pathlib import Path

import numpy as np
import matplotlib as plt
import pandas as pd
import kagglehub

# Download latest version
path = kagglehub.dataset_download("joebeachcapital/30000-spotify-songs")
#path = str(Path.home()) + "/Downloads/30000-spotify-songs"

# settings
QUESTIONS = 5
MAX_ANSWERS_PER_QUESTION = 4

@cache
def start():
    print("##### Welcome To The Grand Spotify Quiz #####")
    print("loading data...")

    df = pd.read_csv(path + "/spotify_songs.csv")

    genres = df["playlist_genre"].unique()
    artists = df["track_artist"].unique()
    albums = df["track_album_name"].unique()

    popular = df[df["track_popularity"] > 75].sort_values(by="track_popularity", ascending=False)
    unpopular = df[df["track_popularity"] < 25].sort_values(by="track_popularity", ascending=True)

    results = []
    categories = np.array(["genres", "artists", "albums", "popular", "unpopular"])

    # start the quiz
    while len(results) < QUESTIONS:
        category = np.random.choice(categories)

        # will ask what genre a song is
        if category == "genres":
            correct = np.random.choice(genres)
            
            songs = df[df["playlist_genre"] == correct]

            song = songs.sample(1)

            print(f"What genre is the song \"{song.iloc[0]["track_name"]}\" by \"{song.iloc[0]["track_artist"]}\"?")

            answers = []
            answers.append(str(correct))
            
            for _ in range(1, MAX_ANSWERS_PER_QUESTION):
                while True:
                    rngGenre = np.random.choice(genres)
                    if rngGenre not in answers:
                        answers.append(str(rngGenre))
                        break

            np.random.shuffle(answers)

            for index, gen in enumerate(answers):
                print(f"{index + 1}. {gen}")
            
            while True:    
                try:
                    userInput = int(input("Enter number $ "))
                    if userInput in range(1, len(answers) + 1):
                        break
                    else:
                        print("Out of range number")
                except:
                    print("Invalid number")
            
            if answers[int(userInput) - 1] == correct:
                print("Correct!")
            else:
                print("Wrong!")
                print(f"{correct}, you chose {answers[int(userInput) - 1]}")
            
            results.append([category, answers[int(userInput) - 1] == correct, correct, answers[int(userInput) - 1]])
        
        # users is shown 4 songs and have to guess the song based on the artist
        # if category == "artists":
        #     artist = np.random.choice(artists)
            
        #     correct = np.random.choice(df[df["track_artist"] == artist])
        #     songs = df[df["track_artist"] != artist]
            
            
    
    # calculate results
    resultDf = pd.DataFrame(results)
    succussCount = resultDf[1].value_counts().get(True, 0)
    succussRate = (succussCount / len(resultDf)) * 100
    
    print(f"You got {succussCount}/{len(resultDf)}, thats a score of {succussRate}%")
            



start()