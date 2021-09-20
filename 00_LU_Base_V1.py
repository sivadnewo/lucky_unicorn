import random

def show_instructions():
    print("just spend all your money here okay... thanks. good luck.")
    print()


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






# Main routine goes here
print("Welcome to the Lucky Unicorn")
print()
rounds_played = 0
# Ask user if played before
played_before = input("Have you played this game before?").lower()
print()
if played_before == "no":
    show_instructions()
elif played_before == "yes":
    print("program continues")
else:
    "Please enter yes or no"
# If they say no, output 'display instructions'

# ask user how much
how_much = number_check("how much would you like to play with? ", 0 ,10)
print()
print("you will be spending ${}".format(how_much))
print()
balance = how_much
# token generator
play_again = input("Press <Enter> to play...").lower()
print()
while play_again == "":
    rounds_played += 1
    print("*** Round #{} ***".format(rounds_played))

    chosen_num = random.randint(1, 100)
    # adjusting balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36    :
        chosen = "donkey"
        balance -= 1
    else:
        if chosen_num % 2 == 0:
            chosen = "zebra"
        else:
            chosen = "horse"
    balance -=0.5

    print("You got a {} Your balance is ${:.2f}".format(chosen, balance))



    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("press Enter to play again"
                       "or 'xxx' to quit")
        print()


print()
print("Final balance ${:.2f}".format(balance))


