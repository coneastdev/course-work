import random

def calc_cehcksum(digits: list):
    sum = 0
    for index, digit in enumerate(digits):
        sum += ((index + 1) * int(digit))
    
    checksum = sum % 10
    return checksum

def check_id(id: int | str) -> bool:
    try:
        id = int(id)
        id = str(id)
    except:
        return False
    if len(id) == 7:
        digits = list(id)
        last_digit = str(digits[-1])
        digits.pop()
        checksum = calc_cehcksum(digits)

        if last_digit == str(checksum):
            print(f"INFO: ID valid, checksum {last_digit} = {checksum}")
            return True
        else:
            print(f"ERROR: ID does not equal check sum, {last_digit} ≠ {checksum}")
            return False

    print("ERROR: ID is does not have length of 7")
    return False

def gen_id():
    digts = []
    for _ in range(6):
        num = random.randint(1, 9)
        digts.append(num)
    
    checksum = calc_cehcksum(digts)
    digts.append(checksum)

    return "".join(digts)

def main():
    print("##### parcel ID checker/generator ######")
    print("1. check ID\n2. gen ID")
    user_input = input("Enter option number $ ")
    if user_input == "1"
        if check_id(input("Enter ID to check $ ")) == True:
            print("Valid ID")
        else:
            print("Invalid ID")
    elif user_input == 2:
        print(f"ID: {gen_id()}")

    if input("Continue Y/n? $ ").lower != "y":
        main()
    else:
        quit()

if __name__ == "__main__":
    main()