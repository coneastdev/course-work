import math

def energyLevlsArr():
    energyLevels = [1, 2 ,3, 4, 5]

    print(energyLevels)
    print(energyLevels[0], energyLevels[math.floor(len(energyLevels) / 2)], energyLevels[-1])
    energyLevels[4] = -5
    print(energyLevels)

def usernamesArr():
    usernames = ["john123", "mark842", "jane7402"]

    print(usernames)
    print(usernames[0], usernames[math.floor(len(usernames) / 2)], usernames[2])
    usernames[1] = "842mark"
    print(usernames)

def stepsArr():
    steps = [602, 1360, 2039, 423]

    print(steps)
    print(steps[0], steps[math.floor(len(steps) / 2)], steps[-1])
    steps[1] = 1630
    print(steps)

def task1():
    energyLevlsArr()
    usernamesArr()
    stepsArr()

def task2():
    screenTimes = [120, 95, 140, 160, 80, 100, 200]

    print(screenTimes[2])

    print(sum(screenTimes[0:3]) // 3)

    screenTimes[-1] = 150
    
    print(max(screenTimes), ", ", min(screenTimes))

def task3():
    listA = [1, 2, 3]
    listB = [1, "2", 3.0]

    print(listA, listB)

    print(sum(listA))
    try:
        print(sum(listB))
    except:
        print("You cannot use sum on arrays with strings")
    
    print("A traditional array is fixed in size both in length and the bit size of items and can be indexed with a intiger.")

def task4():
    notifications = [34, 28, 55, 40, 60, 22, 18]
    highst = 0
    lowst = 0
    for i, n in enumerate(notifications):
        if notifications[highst] < n:
            highst = i
        if notifications[lowst] > n:
            lowst = i
        print(n)
    print(f"\nThe highst is {notifications[highst]}, the lowst is {notifications[lowst]}. The total is {sum(notifications)} and the mean average is {round(sum(notifications) / len(notifications))}")

    while True:
        try:
            notifications.append(int(input("\nEnter new notification value $ ")))
            break
        except:
            print("\nInvalid number, try again")

    print(notifications)
    
    notificationsA = [13, 15, 60, 30 ,23]
    notificationsB = [0, 30, 23, 50, 30]

    print(f"\nUser A has a total of {sum(notificationsA)}, where as user B has a total of {sum(notificationsB)}. User A has an average of {sum(notificationsA) / len(notificationsA)} where as user B has an average of {sum(notificationsB) / len(notificationsB)}.")

# task1()
# task2()
# task3()
# task4()