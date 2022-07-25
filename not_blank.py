# input_checker

# Checks that response is not blank or numbers
def input_checker(question, error_message):
    valid = False

    while not valid:
        response = input(question) # Ask the user for an input

        if response.isdigit() or response == "": #Checks if the response is a digit or blank
            print(error_message)
        else:
            return response

for item in range(0,3):
    main_text = input_checker("Input the text: ", "Please enter a text that isn't a number or blank") # Runs the function
    print(main_text)