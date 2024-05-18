import random
from rich import print

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

print('for ✂️  press r')
print('for 📄 press f')
print('for 🪨  press c')
print('to [blue3]quit[/blue3] press q')

while True:
    user_input = input('Your choice is: ')
    if user_input == "q":
        break

    if user_input == "r":
        user_input = 'rock'

    if user_input == "f":
        user_input = 'paper'
    
    if user_input == "c":
        user_input = 'scissors'

    if user_input not in options:
        continue
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_action = options[random_number]

    if user_input == computer_action:
        print(f"Both players selected {user_input}. It's a [purple]tie![/purple]")
        computer_wins += 1
        user_wins += 1
    elif user_input == 'rock':
        if computer_action == 'scissors':
            print("Computer picked [dark_orange]scissors[dark_orange] You [green]win![/green]")
            user_wins += 1
        else:
            print("Computer picked [grey35]rock![/grey35] You [red]lose.[/red]")
            computer_wins += 1
    elif user_input == 'paper':
        if computer_action == 'rock':
            print("Computer picked [grey35]rock[/grey35] You [green]win![/green]")
            user_wins += 1
        else:
            print("Computer picked [white]paper[/white] You [red]lose.[/red]")
            computer_wins += 1
    elif user_input == 'scissors':
        if computer_action == 'paper':
            print("Computer picked [white]paper[/white] You [green]win![/green]")
            user_wins += 1
        else:
            print("Computer picked [dark_orange]scissors[dark_orange] You [red]lose.[/red]")
            computer_wins += 1

print("You [green]won![/green]", user_wins, "times.")
print("The computer [green]won![/green]", computer_wins, "times.")
print("Goodbye!")