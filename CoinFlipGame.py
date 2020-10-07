from person import Person
from coin import Coin

print("Coin Flip Game!\n")
name = input("What is your name? ")
player_choice: str
computer_choice: str

# Loop forever getting input from player until it's a valid choice
while True:
    player_choice = input("Choose Heads or Tails: ")
    if player_choice == "Heads" or player_choice == "Tails":
        break

# The computer chooses the opposite of the player
computer_choice = "Heads" if player_choice == "Tails" else "Tails"

# Create a Person object for the player with their name and choice
player1 = Person(name, player_choice)

# Create a person object for the computer
player2 = Person("Computer", computer_choice)

# Create a coin object
coin = Coin()

# Flip the coin and store the result
outcome = coin.flip()

# Print the outcome
if outcome == player1.chosen_side:
    print(player1.name + " wins the toss with a " + outcome)
else:
    print(player2.name + " wins the toss with a " + outcome)