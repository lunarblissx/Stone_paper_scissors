import random

print("STONE PAPER SCISSORS GAME")
print("Instructions:")
print("1. Paper wraps Stone")
print("2. Stone destroys Scissors")
print("3. Scissors cut Paper")

choices = ("STONE", "PAPER", "SCISSORS")

# Dictionary storing what each choice defeats
wins = {
    "STONE": "SCISSORS",
    "PAPER": "STONE",
    "SCISSORS": "PAPER"
}

no_of_guesses = 10
you_won = 0
system_won = 0
draws = 0

while True:

    inp = input("\nEnter your choice: ").upper()

    if inp not in choices:
        print("Invalid input! Please enter STONE, PAPER or SCISSORS.")
        continue

    computer = random.choice(choices)

    print("Computer chose:", computer)

    if inp == computer:
        print("DRAW!")
        draws += 1

    elif wins[inp] == computer:
        print("Congratulations! You won!")
        you_won += 1

    else:
        print("You lost!")
        system_won += 1

    no_of_guesses -= 1
    print("Guesses left:", no_of_guesses)

    if no_of_guesses == 0:
        print("\n========== GAME OVER ==========")
        print("You won:", you_won)
        print("System won:", system_won)
        print("Draws:", draws)

        if you_won > system_won:
            print("🏆 You are the Overall Winner!")
        elif system_won > you_won:
            print("💻 System Wins!")
        else:
            print("🤝 Overall Draw!")

        break