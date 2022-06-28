def num_check(question, error, num_type):
    valid = False
    while not valid:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
            else:
                return response
        
        except ValueError:
            print(error)


    # Get key (between 1 and 25)
    key = num_check("Input key: ")

# check that key is valid...
    if key < 1:
        print("Sorry you are too young for this movie")
        #FIX
    elif key > 25:
        print("That is very old - it looks like a mistake")
        #FIX