

def choices_checker(question, choices):

    valid = False
    while not valid:

        response = input(question).lower()

        for var_item in choices:
            if response == var_item:
                return response
            elif response == var_item[0]:
                return var_item

        print("Please enter a valid choice.\n")

choices = ["encrypt","decrypt"]

choices_checker("Do you want to encrypt/decrypt?", choices)