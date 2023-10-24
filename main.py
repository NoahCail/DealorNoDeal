import random as r

case_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]

case_values = [0.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 
               75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

personal_case_number = 0
personal_case_value = 0

def personal_case_process():
    selection = input("What case would you like to select to hold on to throughout the game?: ")
    if int(selection) in case_numbers:
        personal_case_number += int(selection)
        value = r.choice(case_values)
        personal_case_value += value
        case_numbers.remove(int(selection))
        case_values.remove(value)

def round_process():
    print("Remaining Cases:\n", case_numbers)
    print("\nRemaining Values:\n", case_values)
    selection = input("\nWhat case would you like to select?: ")
    if int(selection) in case_numbers:
        case_numbers.remove(int(selection))
        value = r.choice(case_values)
        print("\nCase #" + str(int(selection)) + "'s value was " + str(value) + "!\n")
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
    

personal_case_process()

#Round 1
for i in range(6):
    round_process()

round_1_answer = banker_process(case_values)

if round_1_answer == "N":
    for i in range(5):
        round_process()

round_2_answer = banker_process(case_values)

if round_2_answer == "N":
    for i in range(4):
        round_process()

round_3_answer = banker_process(case_values)

if round_3_answer == "N":
    for i in range(3):
        round_process()

round_4_answer = banker_process(case_values)

if round_4_answer == "N":
    for i in range(2):
        round_process()

round_5_answer = banker_process(case_values)

if round_5_answer == "N":
    round_process()

round_6_answer = banker_process(case_values)

if round_6_answer == "N":
    round_process()

round_7_answer = banker_process(case_values)

if round_7_answer == "N":
    round_process()

round_8_answer = banker_process(case_values)

if round_8_answer == "N":
    round_process()