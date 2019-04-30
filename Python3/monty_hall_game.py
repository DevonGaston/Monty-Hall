from random import choice
def monty_hall(doors):
    prize = choice(doors)
    print("[A] Door One")
    print("[B] Door Two")
    print("[C] Door Three")
    print("Please enter your choice: ")
    answer = input().upper()
    if answer not in doors:
        print("Sorry, that's not one of the doors we have.  Here, we'll "
              + "select one for you!")
        answer = choice(doors)
        print("We gave you door " + answer + ".  Hope it works out for you!")

    if answer == prize:
        remaining = list(set(doors) - set(prize))
        open_door = choice(remaining)
        alternate_door = choice(list(set(remaining) - set(open_door)))
    else:
        open_door = choice(list(set(doors)- set(answer) - set(prize)))
        alternate_door = prize

    print("Door opened is " + open_door + "...it's a goat."
          + "Would you like to switch doors?  (Y/N)")
    switch_door = input()
    if switch_door.upper() == "Y":
        print("You traded door " + answer + " for door " + alternate_door + ".")
        if alternate_door != prize:
            print("The door contains.....a goat.  It's no car, but ride it into battle"
                  + " and conquer your foes!")
        else:
            print("The door contains....a car!  Congrats, you won...shame it has no"
                  + " gas in it.")
    else:
        print("You kept door " + answer + ".")
        if answer != prize:
            print("The door contains.....a goat.  It's no car, but ride it into battle"
                  + " and conquer your foes!")
        else:
            print("The door contains....a car!  Congrats, you won...shame it has no"
                  + " gas in it.")
    print("Would you like to play again? (Y/N)")
    play_again = input()
    if(play_again.upper() == "Y"):
        monty_hall(doors)
    else:
        print("Thank you for playing!")
