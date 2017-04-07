def gameMode():

    gameModeChoiceState = "False"

    print("Would you like to play True or False or RPG?")  # Asks the user which game mode they would like to play

    while gameModeChoiceState == "False":

        gameModeChoice = input("Selection t/f or rpg?: ")  # Takes the input for their selection

        gameModeChoice.lower()  # Converts the input to a lowercase version

        if gameModeChoice == "t/f":
            tf()  # If the user chooses the true or false it runs that function


        elif gameModeChoice == "rpg":
            rpg()  # If the user chooses the RPG it runs that function

        else:
            print("\nPlease input a vaild choice!\n")


def tf():

    x = 0

    answer1state = "False"
    answer2state = "False"
    answer3state = "False"
    answer4state = "False"
    answer5state = "False"
    answer6state = "False"
    answer7state = "False"
    answer8state = "False"
    answer9state = "False"
    answer810state = "False"

    print("You have selected True or False")

    # *****************************************************************************

    while answer1state == "False":

        print("\nThe Symbol for Uranium is Ur?")

        answer1 = input("Answer: ")

        if answer1 == "false":

            answer1state = "True"

            print("You got the answer correct!")

            x = 0

        elif answer1 != "false":
            print("\nYou got the answer wrong. Try again")

            x += 1

            if x == 5:
                print("\nYou get a hint!\n")

                print("There is only one letter in the symbol for Uranium")

    # *****************************************************************************

    while answer2state == "False":

        print("\n\nThe Atomic mass of Uranium is greater than 200?")

        answer1 = input("Answer: ")

        if answer1 == "true":

            answer2state = "True"

            print("You got the answer correct!")

            x = 0

        elif answer1 != 'true':
            print("\nYou got the answer wrong. Try again")

            x += 1

            if x == 5:
                print("\nYou get a hint!\n")

                print("The Atomic Mass of uranium is approximately 238")

    # *****************************************************************************

    while answer3state == "False":

        print("\n\nIs uranium toxic?")

        answer1 = input("Answer: ")

        if answer1 == "true":

            answer3state = "True"

            print("You got the answer correct!")

            x = 0

        elif answer1 != 'true':
            print("\nYou got the answer wrong. Try again")

            x += 1

            if x == 5:
                print("\nYou get a hint!\n")

                print("Uranium will damage the human body")

    # *****************************************************************************

    while answer4state == "False":

        print("\n\nThe human body contains uranium?")

        answer1 = input("Answer: ")

        if answer1 == "true":

            answer4state = "True"

            x = 0

            print("You got the answer correct!"
                  "Fact:"
                  "\tYour body contains .0001mg of uranium!")

        elif answer1 != 'true':
            print("\nYou got the answer wrong. Try again")

            x += 1

            if x == 5:
                print("\nYou get a hint!\n")

                print("Even though it is toxic it is found in most animals ")

    # *****************************************************************************

    while answer5state == "False":

        print("\n\nThe human body contains uranium?")

        answer1 = input("Answer: ")

        if answer1 == "true":

            answer4state = "True"

            x = 0

            print("You got the answer correct!"
                  "Fact:"
                  "\tYour body contains .0001mg of uranium!")

        elif answer1 != 'true':
            print("\nYou got the answer wrong. Try again")

            x += 1

            if x == 5:
                print("\nYou get a hint!\n")

                print("Even though it is toxic it is found in most animals ")

    # *****************************************************************************

    while answer6state == "False":

        print("\n\nThe human body contains uranium?")

        answer1 = input("Answer: ")

        if answer1 == "true":

            answer4state = "True"

            x = 0

            print("You got the answer correct!"
                  "Fact:"
                  "\tYour body contains .0001mg of uranium!")

        elif answer1 != 'true':
            print("\nYou got the answer wrong. Try again")

            x += 1

            if x == 5:
                print("\nYou get a hint!\n")

                print("Even though it is toxic it is found in most animals ")

    # *****************************************************************************









def rpg():

    print("You have selected RPG\n")


print(">>> Uranium Game\n")

print("Hello and welcome to the Uranium Game\n")  # This introduces the user to the game

gameMode()
