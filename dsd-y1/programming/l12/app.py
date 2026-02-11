def songthing():
    songs = []

    loops = 5
    loop = 0

    while loops > 0:
        songs.append(input("Enter song name $ "))
        loops -= 1
        

    print(songs)

    if input("Want to modify songs? y/n $ ").lower() == "y":
        while True:
            for index, song in enumerate(songs):
                print(f"{index + 1}. {song}")
            try:
                i = int(input("Enter song number to remove $ ")) - 1
                songs.remove(songs[i])
            except:
                print("Invalid song")
            if input("Continue? y/n").lower() != "y":
                break

    songs.sort()

    print(songs)

def cini(movies: list):
    print("\n----- MOVIE-NATOR 9000 -----\n1. veiw movies\n2. add movie\n3. remove movie\n4. find movie\n5. exit\n")
    match input("Select option $ "):
        case "1":
            print("\n")
            moviesToPrint = ""
            for index, movie in enumerate(movies):
                moviesToPrint += f"{index}. {movie},"
            input("Press enter to continue")
        case "2":
            movies.append(input("Enter movie name $ "))
        case "3":
            for index, movie in enumerate(movies):
                print(f"{index + 1}. {movie}")
            try:
                i = int(input("Enter song number to remove $ ")) - 1
                movies.remove(movies[i])
                print(f"removed {movies[i]}")
            except:
                print("Invalid song")
        case "4":
            search = input("enter song name $ ")
            print("")
            for index, movie in enumerate(movies):
                if search in movie:
                    print(f"{index}. {movie}")
            input("Press enter to continue")
        case "5":
            exit()
    cini(movies)

cini(movies=["nightmare before christmas", "beetle juice", "michial miers", "screem", "nightmare on elm street"])