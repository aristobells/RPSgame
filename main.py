import random
possible_option ={"R":"Rock", "P":"Paper","S":"Scissors"}
tie = True
while tie:
    user = input("What do you choose? Type 'R' for Rock, 'P' for Paper and 'S' for Scissors:   ").upper()
    while user not in possible_option:
        print("Error! Enter a valid option")
        user = input("What do you choose? Type 'R' for Rock, 'P' for Paper and 'S' for Scissors:   ").upper()
    computer = random.choice(list(possible_option))
    print(f"player({possible_option[user]}) : Computer({possible_option[computer]})")
    if user == "R" and computer == "S":
        print("You win!")
        break
    elif user == "P" and computer == "R":
        print("You win!")
        break
    elif user == "S" and computer == "P":
        print("You win!")
        break
    elif user == computer:
        print("Tie")
        tie = True
    else:
        print("Computer won")
        break






