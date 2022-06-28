import re
from urllib import response

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

# Encrypt or Decrypt
def encrypt_decrypt(question):

    to_check = ["encrypt","decrypt"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter either encrypt or decrypt.\n")

# Key
def ask_key(question):

    to_check = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","16","17","18","19","20","21","22","23","24","25"]

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in to_check:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please choose a valid key ranging from 1-25\n")

# Cipher Text
def cypher(target, shift):
    for index in range(len(alphabet)):
        if alphabet[index] == target:
            x = index + shift
            y =  x % len(alphabet)
            return (alphabet[y])

# Main Routine goes here
alphabet = "abcdefghijklmopqrstuvwxyz"

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
method = encrypt_decrypt("Do you want to decrypt or encrypt the text?")

if method == "decrypt":
    print("You have chose to decrypt the message.\n")    
    shift = ask_key("Please input the key you desire")

    print("Your key is {}".format(shift))
    encrypted_string = ""
    for x in main_text:
        if x == ' ':
            encrypted_string += ' '
        else:
            encrypted_string += cypher(x, shift)

    print("This is the text:\n{}".format(encrypted_string))

