import random as r

#TODO: Add in testing by using try syntax



#List of all the brief case numbers
case_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

#List of all the values within the brief cases
case_values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 
               75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

#Placeholder variables meant to store the number and value of the players selected personal brief case
personal_case_number = 0
personal_case_value = 0

#
countdown = 6

#Function that reports the current remaining cases
def current_cases(case_numbers, case_values):
    
    print("Remaining Cases:\n", case_numbers, "\nRemaining Values:\n", case_values)

#Function for having the player select their personal case
def personal_case_process(case_number):

    selection = int(input("Which of these cases do you think has the million dollars in it?: "))
    if selection in case_numbers:
        case_number += selection
        case_numbers.remove(selection)

#Funtion for having the player select a case to eliminate from the board
def round_process():

    current_cases(case_numbers, case_values)
    selection = int(input("\nWhat case would you like to select?: "))
    if selection in case_numbers:
        case_numbers.remove(selection)
        value = r.choice(case_values)
        print("\nCase #" + str(selection) + "'s value was " + str(value) + "!\n")
        case_values.remove(value)
    else:
        print("\nPlease choose a case number from the list of case numbers shown below:\n")
        round_process()

#Function that generates an offer from the banker for the player to review and decide on
def banker_process(values):

    offer = int(sum(values) / len(values))
    current_cases(case_numbers, case_values)
    print("\nAt this time the banker is willing to offer you $" + str(offer) + " to walk away!\nWould you like to take this deal?\n")
    response = input("Y or N: ").upper()
    if response == "Y":
        print("\nCongrats you have won $" + str(offer), "\nThanks for playing!")
    elif response == "N":
        print("\nAlright then the game continues!\n")
    else:
        print("\nPlease only answer with a Y or N")
        banker_process(case_values)
    return response

#Function that starts the game and progresses it through as the player makes selections
def game_play(values, countdown):
    
    for i in range(countdown):
        round_process()

    answer = banker_process(values)

    if answer == "N":
        if countdown > 1:
            countdown -= 1
            game_play(values, countdown)
        elif len(values) > 2:
            game_play(values, countdown)
        elif len(values) == 2:
            print("You are now down to the final 2 cases!\n")
            final_answer = int(input("Would you like to stick with your personal case #" + str(personal_case_number) + " or switch to the last remaining case #" + str(case_numbers[0] + "?: ")))
            if final_answer == personal_case_number:
                print("Alright it is time to finally open your case and see what you have been holding on to this whole game!\n")
                print("Congrats you won $" + str(r.choice(values)) + "!")
            elif final_answer == case_numbers[0]:
                print("Alright it is time to finally open the last case and see what you have won!\n")
                print("Congrats you won $" + str(r.choice(values)) + "!")
            #else:
                #Work on this part, probably need to create this into a function so it can be restarted on its own
        else:
            game_play(values, countdown)
    # elif answer == "Y":
    #     replay = input("Would you like to play again? Y or N?: ").upper()
    #     if replay == "Y":
    #         countdown = 6
    #         personal_case_process()
    #         game_play()
            
personal_case_process(personal_case_number)

game_play(case_values, countdown)
