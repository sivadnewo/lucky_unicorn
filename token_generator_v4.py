import random

# main rourine goes here

STARTING_BALANCE = 100
balance = STARTING_BALANCE

# testing loop to generate 20 tokens
for item in range (0, 100):
    chosen_num = random.randint(1, 100)
# adjusting balance
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        balance -= 1
    else:
       if chosen_num % 2 == 0:
           chosen = "zebra"
           balance -= 0.5
       else:
           chosen = "horse"
           balance -=0.5
    #output
    print("You got  a {}.  Your balance is "
          "${:.2f}".format(chosen, balance))

    print()
    print("Starting Balance ${:.2f}".format(STARTING_BALANCE))
    print("Final Balance ${:.2f}".format(balance))
