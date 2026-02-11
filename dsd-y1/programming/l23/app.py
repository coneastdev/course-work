# import csv

# with open("./dsd-y1/l23/scores.csv", "a", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerow(["alex", "10"])

import csv

FILENAME = "./dsd-y1/l23/scores.csv"

def add_score(username, score):
    # TODO: Append username and score to the CSV file
    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, score])

def show_scores():
    # TODO: Read all scores from the CSV file and print them
    print("\nSCORES:")
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0] + ": " + str(row[1]))
        

def main():
    while True:
        print("\n1. Add score")
        print("2. Show all scores")
        print("3. Quit")
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Enter username: ")
            score = int(input("Enter score: "))
            add_score(username, score)
        elif choice == "2":
            show_scores()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()