# not_blank

# Checks that response is not blank
def not_blank(question, error_message):
    valid = False

    while not valid:
        response = input(question)

        if response != "":
            return response
        else:
            print(error_message)

not_blank("Enter any text: ", "Invalid")