# Check if the number is valid
from numpy import number


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

for item in range(0, 4):
    number_checker("Input a number: ")