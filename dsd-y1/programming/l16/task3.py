import os
import random

quizs = {
    "music": {
        "Which bettle song mocked the beach boys": {
            "tags": ["beatles", "60s", "rock"],
            "corect": "Back in the USSR",
            "incorect": ["Here comes the sun", "Ocotpus garden", "Jude", "Shout"]
        },
        "Who won Eurovison 2025": {
            "tags": ["eurovision", "2020s", "pop"],
            "corect": "JJ",
            "incorect": ["Tommey Cash", "Yuval Raphael", "KAJ", "Miriana Conta"]
        },
        "Which of these names are in the Mambo number 5": {
            "tags": ["mambo", "90s", "pop"],
            "corect": "Lisa",
            "incorect": ["Margret", "May", "Cate", "Pam"]
        },
        "Who sung \"Boys don't cry\"": {
            "tags": ["80s", "rock", "new wave", "the cure"],
            "corect": "The Cure",
            "incorect": ["Blur", "Saint Motel", "Maroon 5"]
        },
        "Which of these is not sung by the artic monkeys": {
            "tags": ["arctic monkeys", "2000s", "rock"],
            "corect": "I was made for loving you",
            "incorect": ["Room 505", "I bet you look good on the dance floor", "Flurencent adolecence"]
        },
        "Which of these is not sung by the Electric Lights Orchestra": {
            "tags": ["electric light orchestra", "elo", "70s", "rock"],
            "corect": "While my guitar gently weeps",
            "incorect": ["Livin' Thing", "Last Train to London", "Telephone Line", "Mr. Blue Sky", "Turn to Stone"]
        }
    },
    "programming": {
        "Which programming language is useed for minecraft modding": {
            "tags": ["programming", "languages", "minecraft", "modding"],
            "corect": "Java",
            "incorect": ["JavaScript", "Python", "C++", "Ruby"]
        },
        "Which programming language uses the walrus symbol the most ( := )": {
            "tags": ["programming", "languages", "walrus", "symbol"],
            "corect": "Go",
            "incorect": ["Java", "JavaScript", "C++", "Ruby"]
        },
        "Which of these is not a programming language": {
            "tags": ["programming", "languages", "not a language"],
            "corect": "React",
            "incorect": ["TypeScript", "flutter", "swift", "kotlin"]
        },
        "What does the T in T3 stack stand for": {
            "tags": ["programming", "youtuber", "frontend", "nextjs"],
            "corect": "Theo",
            "incorect": ["TypeScript", "Type", "Testing", "Translation", "Tod Howard"]
        },
        "Which frontend framework allows you to use other fron end frameworks": {
            "tags": ["programming", "js", "frontend", "astrojs"],
            "corect": "Astro JS",
            "incorect": ["React", "SVlite", "Vue", "solid js", "preact"]
        }
    },
    "linux": {
        "Which of these is not a real linux distro to setup": {
            "tags": ["linux", "funny"],
            "corect": "Micheal Jackson Linux",
            "incorect": ["AmongOS", "WuBuntu", "POP", "Hanna Montana Linux", "Justin Bieber Linux"]
        },
        "Which of these dsitros is the hardst": {
            "tags": ["linux"],
            "corect": "GenToo",
            "incorect": ["Arch", "NixOS", "RedHat OS", "Rockey Linux", "Open Suse"]
        },
        "What is the name of the most popular virtual keyboard on Linux": {
            "tags": ["linux"],
            "corect": "IBus",
            "incorect": ["KVK", "open keyboard", "GNU board"]
        }
    }
}

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
   
def play(questions):
    maxPoints = len(questions)
    points = 0
    while len(questions) > 0:
        question = random.choice(list(questions.items()))[0]
        quests = []
        quests.append(questions[question]["corect"])
        for wrong in questions[question]["incorect"]:
                quests.append(wrong)
        print(quests)
        random.shuffle(quests)
        clear()
        print(question)
        print("")
        for index, quest in enumerate(quests):
            print(f"{index}. {quest}")
        select = input("\nSelect option $ ")
        try:
            if quests[int(select)] == questions[question]["corect"]:
                points += 1
                print("corect")
                input("Press enter for next $ ")
            else:
                print("incorect")
                input("Press enter for next $ ")
        except:
            print("invalid input, skiping question")
            input("Press enter for next $ ")
        questions.pop(question)
    clear()
    print(f"You have completed the quiz\n\nYou scored {points}/{maxPoints}")
    input("Press enter to return to menu $ ")
        
def main(quizs):
    clear()
    print("##### Quiz-a-tron 9000 #####")
    print("1.play all quizs\n2.select quizs\n3.exit")
    match input("Enter option number $ "):
        case "1":
            questions = {}
            for cat in quizs:
                for question in quizs[cat]:
                    questions[question] = quizs[cat][question]
            play(questions)
        case "2":
            for cat in quizs:
                print(cat)
            quiz = []
            while True:
                print(f"You have selected ({quiz})")
                quiz.append(input("select quiz to add $ "))
                if input("continue? Y/n $ ").lower() != "y":
                    break
            questions = {}
            for cat in quiz:
                for question in quizs[cat]:
                    questions[question] = quizs[cat][question]
            play(questions)
        case "3":
            exit()

    main(quizs)
    
if __name__ == "__main__":
    main(quizs)