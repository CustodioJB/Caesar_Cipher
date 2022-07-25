# string_checker

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


choice = string_checker("Do you want to encrypt or decrypt the text?", ["encrypt", "decrypt"], "Please enter a valid choice")

print("You chose to {} the text".format(choice))