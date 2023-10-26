import random as r

case_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

case_values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 
               75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

personal_case_number = 0
personal_case_value = 0
countdown = 6

def personal_case_process(case_number):
    selection = int(input("What case would you like to select to hold on to throughout the game?: "))
    if selection in case_numbers:
        case_number += selection
        case_numbers.remove(selection)

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

def round_process():
    print("Remaining Cases:\n", case_numbers)
    print("\nRemaining Values:\n", case_values)
    selection = int(input("\nWhat case would you like to select?: "))
    if selection in case_numbers:
        case_numbers.remove(selection)
        value = r.choice(case_values)
        print("\nCase #" + str(selection) + "'s value was " + str(value) + "!\n")
        case_values.remove(value)
    else:
        print("\nPlease choose a case number from the list of case numbers shown below:\n")
        round_process()

def banker_process(values):
    total = 0
    for i in values:
        total += i
    offer = int(total / len(values))
    print("Remaining Cases:\n", case_numbers)
    print("Remaining Values:\n", case_values)
    print("\nBased on what the banker has seen they are willing to offer you $" + str(offer) + " at this time to walk away!\n")
    print("Would you like to take this deal?")
    response = input("Y or N: ").upper()
    if response == "Y":
        print("\nCongrats you have won $" + str(offer))
        print("\nThanks for playing!")
    elif response == "N":
        print("\nAlright then the game continues!\n")
    else:
        print("\nPlease answer with a Y or N")
        banker_process(case_values)
    return response
    
personal_case_process(personal_case_number)

game_play(case_values, countdown)

