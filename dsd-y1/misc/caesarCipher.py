import re

ALPHABET = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

settings = {
    "text": "",
    "shifts": 0
}

def encode(text: str, shifts: int):
    arr: list = list(text)
    encoded: list[str] = []
    for chr in arr:
        upper: bool = chr.isupper()
        if re.fullmatch(r"^[a-zA-Z]+$", chr):
            for i, v in enumerate(ALPHABET):
                if chr.lower() == v:
                    alphabetNum = i
                    if shifts < 0:
                        for _ in range(shifts * -1):
                            if alphabetNum > 0:
                                alphabetNum -= 1
                            else:
                                alphabetNum = 25
                    elif shifts > 0:
                        for _ in range(shifts):
                            if alphabetNum < 25:
                                alphabetNum += 1
                            else:
                                alphabetNum = 0
                    else:
                        return text
                    if upper:
                        encoded.append(ALPHABET[alphabetNum].upper())
                    else:
                        encoded.append(ALPHABET[alphabetNum])
        else:
            encoded.append(chr)
            pass
    return "".join(encoded)   

def decode(text: str, shifts: int):
    arr: list = list(text)
    decoded: list[str] = []
    for chr in arr:
        upper: bool = chr.isupper()
        if re.fullmatch(r"^[a-zA-Z]+$", chr):
            for i, v in enumerate(ALPHABET):
                if chr.lower() == v:
                    alphabetNum = i
                    if shifts > 0:
                        for _ in range(shifts):
                            if alphabetNum > 0:
                                alphabetNum -= 1
                            else:
                                alphabetNum = 25
                    elif shifts < 0:
                        for _ in range(shifts * -1):
                            if alphabetNum < 25:
                                alphabetNum += 1
                            else:
                                alphabetNum = 0
                    else:
                        return text
                    if upper:
                        decoded.append(ALPHABET[alphabetNum].upper())
                    else:
                        decoded.append(ALPHABET[alphabetNum])
        else:
            decoded.append(chr)
            pass
    return "".join(decoded)

def main():
    print("\n##### Caesar Cipher #####")
    print(f"text: {settings["text"] if settings["text"] != "" else "no text inputed"}")
    print(f"shifts: {settings["shifts"]}")
    print("\n1. encode\n2. decode\n3. change text\n4. change shifts\n")
    inp = input("enter selection number $ ")
    match inp:
        case "1":
            encoded: str = encode(settings["text"], settings["shifts"])
            settings["text"] = encoded
        case "2":
            decoded: str = decode(settings["text"], settings["shifts"])
            settings["text"] = decoded
        case "3":
            while True:
                inp = input("\nenter new text $ ")
                if inp != "":
                    settings["text"] = inp
                    break
                else:
                    print("text cannot be empty, try again")
        case "4":
            while True:
                try:
                    inp = input("\nenter new shift amount $ ")
                    inp = int(inp)
                    settings["shifts"] = inp
                    break
                except:
                    print("shifts must be a whole number, try again")
        case "5":
            with open("./dsd-y1/input.txt", "r") as file:
                encoded: str = encode(file.read(), settings["shifts"])
            with open("./dsd-y1/output.txt", "w") as file:
                file.write(encoded)
    
    main()

if __name__ == "__main__":
    main()