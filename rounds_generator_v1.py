balance = 5

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    rounds_played += 1

    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance:", balance)
    print()



    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("press Enter to play again"
                       "or 'xxx' to quit")


print()
print("Final balance", balance)

