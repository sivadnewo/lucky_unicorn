
show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before?").lower().strip()

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")
        # If they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")
    else:
        print("please type yes or no")
