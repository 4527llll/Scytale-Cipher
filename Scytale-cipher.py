red = "\033[31m"
reset = "\033[0m"

def encrypt(text,key):
    transList = []
    padding_length = (key - len(text) % key) % key
    padded_text = text + " " * padding_length
    for i in range(key):
        transList.append(padded_text[i::key]) # get number by key
    return "".join(transList)

def decrypt(text,key):
    resultList = []
    rows = len(text) // key # get rows by key
    for i in range(rows):
        resultList.append(text[i::rows]) # get number by rows
    return "".join(resultList).strip()

def yesno(filename): # User can choose to upload result to file
    while True:
        choice = input(f"{red}Do you want to output to {filename}.txt? (yes/no):{reset} ").strip().lower()
        if choice in ["yes", "no"]:
            return choice
        print("Please re-enter yes or no")

while True: # choosse encrypt or decrypt
    try:
        lockTF = int(input(f'{red}Enter 1 to encrypt, 2 to decrypt:{reset} '))
        if lockTF in [1, 2]:
            break
        else:
            print("Please enter 1 or 2")
    except ValueError:
        print("Please enter an integer")

if lockTF == 1: # main encryption
    try:
        with open("content.txt", 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {red}content.txt{reset} not found. Please create the file first!")
        exit()
    while True: # key validation cheak
        try:
            key = int(input("Input the key (must be > 0): "))
            if key > 0:
                break
            print("Key must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")
    print("\n--- Encryption Result ---")
    result_text = encrypt(content,key)
    print(result_text)
    print("\n")

    if yesno("encryptionResult") == "yes":
        with open('encryptionResult.txt', 'w', encoding='utf-8') as file:
            file.write(result_text)
        print(f"{red}Write complete. Please check encryptionResult.txt{reset}")

elif lockTF == 2: # main decryption
    try:
        with open("encryptionResult.txt", 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: {red}encryptionResult.txt{reset} not found. Please encrypt a file first!")
        exit()
    while True: # key validation cheak
        try:
            key = int(input("Input the key (must be > 0): "))
            if key > 0:
                break
            print("Key must be greater than 0.")
        except ValueError:
            print("Please enter a valid integer.")
    print("\n--- Decryption Result ---")
    result_text = decrypt(content,key)
    print(result_text)
    print("\n")

    if yesno("decryptionResult") == "yes":
        with open('decryptionResult.txt', 'w', encoding='utf-8') as file:
            file.write(result_text)
        print(f"{red}Write complete. Please check decryptionResult.txt{reset}")