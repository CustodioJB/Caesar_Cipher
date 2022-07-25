import string
import random
import pandas

# Main Function Here

# Checks the response is not blank or numbers
def input_checker(question, error_message):
    valid = False

    while not valid:
        response = input(question) # Ask the user for an input

        if response.isdigit() or response == "": #Checks if the response is a digit or blank
            print(error_message)
        else:
            return response

# Check if the number is valid
def number_checker(question):

    error = "Please enter a whole number between 1 and 25"

    valid = False
    while not valid:
        
        # ask user for number and check it is valid
        try:
            response = int(input(question))
            
            
            if 1 <= response <= 25:
                return response
            else:
                print(error)
            
        except ValueError:
            print(error)

# Ask the user a question
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

# Encrypt or decrypt the text by the user choice
def encrypt_decrypt(text,method,key):    
    
    text_output = ''
    shifted = {}
    # If user choses to encrypt
    if method == "encrypt":

        # Creates dictionary of the shifted alphabet and normal alphabet
        for letters in range(len(string.ascii_lowercase)):
            low_alphabet = string.ascii_lowercase

         # Shifts the characters of the normal alphabet using the key provided and create a shifted alphabet
            shifted[low_alphabet[letters]] = low_alphabet[(letters + key)% len(low_alphabet)] 

        for letters in text:

            # Check the characters in text to see if it's in the dictionary
            if letters in shifted:
                # Adds the shifted letters to the empty string
                text_output = text_output + shifted[letters]
                #print(text_output)
            else:
                text_output = text_output + letters
        return text_output

    # If user choses to decrypt
    if method == "decrypt":

        if key == "brute":
            
            # Dictionary and List
            shift_list = []
            decrypted_list = []

            brute_dictionary = {
                'Shift': shift_list,
                'Decrypted': decrypted_list
            }

            def shift_dictionary(key):
                for i in range(0,26):
                    low_alphabet = string.ascii_lowercase
                    letters = low_alphabet[i]
                    shifted[letters] = low_alphabet[(i + key)% len(low_alphabet)]   

            def decrypt_text(text,i):
                text_output = ''

                for letters in text:
                    if letters in shifted:
                        text_output = text_output + shifted[letters]
                    else:
                        text_output = text_output + letters
                decrypted_list.append(text_output)

            # Calls the function to bruteforce 25 times
            for i in range(1,26):
                shift_dictionary(i)
                shift_list.append(i)
                decrypt_text(text,i)

            # Create data frame for the shifted and the decrypted text
            brute_frame = pandas.DataFrame(brute_dictionary)
            brute_frame.set_index("Shift", inplace=True)

            return brute_frame

        else:
            for letters in range(len(string.ascii_lowercase)):
                low_alphabet = string.ascii_lowercase
                shifted[low_alphabet[letters]] = low_alphabet[(letters - key)% len(low_alphabet)] 

            for letters in text:
                if letters in shifted:
                    text_output = text_output + shifted[letters]
                else:
                    text_output = text_output + letters
            return text_output
    
# Ask for Instructions
want_help = string_checker("Do you want to read the instructions?", ["yes","no"], "Please choose either yes/no")

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

# Ask for the text to decrypt/encrypt
main_text = input_checker("Input the text: ", "Please enter a valid text")
# lowercase the text
main_text = main_text.lower()

# Ask user if they want to decrypt or encrypt the message.
method = string_checker("Do you want to decrypt or encrypt the text?", ["encrypt","decrypt"], "Please enter a valid option")

# If user chose encrypt
if method == "encrypt":

    # Ask if they want to generate a random key
    want_key = string_checker("Do you want to let the program generate a random key for you?", ["yes","no"], "Please enter either yes/no only")

    # If user says no ask for a key
    if want_key == "no":
        shift = number_checker("Please input the key you desire: ")
        print("Your key is {}".format(shift))
    else:
        # Generates a random key from 1 - 25
        shift = random.randint(1,25)
        print("The program chose {}".format(shift))

# If user chose decrypt
elif method == "decrypt":

    # Ask user for a key
    want_key = string_checker("Do you have a key?", ["yes","no"], "Please enter either yes/no only")

    # If user chose no the program will bruteforce
    if want_key == "no":
        shift = "brute"
        print("The program will bruteforce for you instead")
    
    else:
        shift = number_checker("Please input the key you desire: ")
        print("Your key is {}".format(shift))

# Calls in the encrypt and decrypt function
text_output = encrypt_decrypt(main_text,method,shift)

print(text_output)
