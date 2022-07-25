# want_instructions

# Yes/No Checker
def string_checker(question, to_check, error_message):
    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print(error_message)

# Ask for Instructions
for item in range(0, 6):
    want_help = string_checker("Do you want to read the instructions?", ["yes", "no"], "Please enter either a yes / no")

    # Outputs instructions or skips it.
    if want_help == "yes":
        print("****** Ceasar Cipher Tutorial ******\n")
        print("This program is a tool to decrypt/encrypt Caesar Cipher")
        print("1). To first start, input the text that you want to decrypt/encrypt")
        print("2). Choose if you want to encrypt or decrypt the text")
        print("3). If you chose to encrypt, the program will ask for a key which is an integer ranging from 1-25")
        print("4). If you chose to decrypt, the program will ask for a key or you can let the program to generate it for you")
        print("5). After encrypting/decrypting, the text will be shown at the output")
    else:
        print("Skipping Instructions")

