#Functions go here


#Main routine goes here
def number_check(question, low, high):
    error = "please enter a number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low < response <= high:
                return response

            else:
                print(error)

        except ValueError:
            print(error)


how_much = number_check("how much would you like to play with? ", 0 ,10)

print("you will be spending ${}".format(how_much))
