def check_id(id: int | str) -> bool:
    try:
        id = int(id)
    except:
        return False
    if len(str(id)) == 7:
        return True

    return False

def main():
    if check_id(input("Enter ID to check $ ")) == True:
        print("Valid ID")
    else:
        print("Invalid ID")

    if input("Continue Y/n? $ ").lower != "y":
        main()

if __name__ == "__main__":
    main()