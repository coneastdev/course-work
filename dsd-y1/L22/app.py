import json

def getScores():
    try:
        with open("./dsd-y1/L22/scores.json", "r") as f:
            return json.load(f)
    except:
        with open("./dsd-y1/L22/scores.json", "w") as f:
            f.write("[]")
            return []

def saveScores(scores):
    with open("./dsd-y1/L22/scores.json", "w") as f:
        f.write(json.dumps(sorted(scores, key=lambda l:l[1], reverse=True)))

def viewScores(scores):
    for index, score in enumerate(scores):
        print(f"{index + 1}. {score[0]}: {score[1]} points")

def addScore(scores):
    username = input("enter username $ ")
    while True:
        
        try:
            score = int(input("enter score $ "))
            break
        except:
            print("that is not a valid number, try again")

    scores.append([username, score])
    saveScores(scores)
    
def mainMenu():
    scores = getScores()
    print("^*^*^*^*^*^Score Logger^*^*^*^*^*^")
    print("1.view scores\n2.add score\n3.search")

    match input("enter selection $ "):
        case "1":
            viewScores(scores)
        case "2":
            addScore(scores)

if __name__ == "__main__":
    mainMenu()
