from person import Person
from coin import Coin

print("Coin Flip Game\n")
name = input("What is your name? ")

# Loop forever getting input from player until it's a valid choice
while True:
    choice = input("Choose Heads or Tails: ")
    if choice == "Heads" or choice == "Tails":
        break
    
# Create a Person object for the player with their name and choice
player = Person(name, choice)
print(player.name + player.chosen_side)