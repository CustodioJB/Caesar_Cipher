import re
from urllib import response
import random

# Functions go here

# Yes/No Checker
def yes_no(question):

    to_check = ["yes","no"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either yes or no...\n")

# Checks that response is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)

# Check if the choice is valid
def choices_checker(question, choices):

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in choices:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either encrypt or decrypt.\n")

# Ask for key
def ask_key(question):

    error = "Please enter a whole number between 1 and 25"

    valid = False
    while not valid:
        
        # ask user for number and check it is valid
        try:
            response = int(input(question))
            
            if response <= 0:
                print(error)
            else:
                return response
            
            if 1 <= response <= 25:
                return response
            else:
                print(error)
            
        except ValueError:
            print(error)

# Encrypting Text
def encrypt(text, shift):
    encrypted_text = ''
    for i in range(len(text)):
        if text[i] == ' ':
            encrypted_text = encrypted_text + text[i]
        elif text[i].isupper():
            encrypted_text = encrypted_text + chr((ord(text[i])+shift-65)%26+65)
        else:
            encrypted_text = encrypted_text + chr((ord(text[i])+shift-97)%26+97)
    return encrypted_text

# Decrypting Text
def decrypt(encrypt_text, shift):
    decrypted_text = ''
    for i in range(len(encrypt_text)):
        if encrypt_text[i] == ' ':
            decrypted_text = decrypted_text + encrypt_text[i]
        elif encrypt_text[i].isupper():
            decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-shift-65)%26+65)
        else:
            decrypted_text = decrypted_text + chr((ord(encrypt_text[i])-shift-97)%26+97)
    return decrypted_text
    
# Main Routine goes here

# Ask for Instructions
want_help = yes_no("Do you want to read the instructions?")

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

# Ask user to input a message
main_text = not_blank("Input the text: ", "Please enter a valid text")


# Ask user if they want to decrypt or encrypt the message.
to_check = ["encrypt","decrypt"]
method = choices_checker("Do you want to decrypt or encrypt the text?", to_check)

# Ask user for a key
want_key = yes_no("Do you want to let the program generate a random key for you?")

if want_key == "no":
    shift = ask_key("Please input the key you desire: ")
    print("Your key is {}".format(shift))
else:
    # Generate a random key from 1 - 25
    shift= random.randint(1,25)
    print("The program chose {}".format(shift))



# If user chose to decrypt the text
if method == "decrypt":
    print("You have chose to decrypt the message.\n")
    print("Decrypting this text: --{}--".format(main_text))
    decrypt_text = decrypt(main_text, shift)
    print("Decrypted text: {}".format(decrypt_text))

# If user chose to encrypt the text
elif method == "encrypt":
    print("You have chose to encrypt the message.\n")
    print("Encrypting this text: {}".format(main_text))
    encrypted_text = encrypt(main_text, shift)
    print("Encrypted text: {}".format(encrypted_text))