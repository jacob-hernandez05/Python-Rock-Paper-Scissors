# Imports and assigns all necessary variables in order for the game to run.
import random
choices = ["rock", "paper", "scissors"]
playerScore = 0
botScore = 0
playerName = input("What is your name? ")

# Loop used for game to run aslong as the player continues playing
while True:
  # .lower() used to prevent errors within the program, turns all input lowercase
  playerChoice = input("Welcome to Rock, Paper, Scissors! Enter a choice (or 'quit') to exit: ").lower()
  if playerChoice == "quit":
    break
  if playerChoice not in choices:
    print("Invalid selection. Try again.")
    continue
  # Allows for computer to choose random choice out of the list
  computer = random.choice(choices)
  print("Computer chose " + computer)

  if playerChoice == computer:
    print("It's a tie!")
  elif playerChoice == "rock" and computer == "scissors" or playerChoice == "paper" and computer == "rock" or playerChoice == "scissors" and computer == "paper":
    print("You win!")
    playerScore += 1
    print("Player: " + str(playerScore) + " Bot: " + str(botScore))
  else:                        
    print("Computer wins!")
    botScore += 1
    print("Player: " + str(playerScore) +  " Bot: " + str(botScore))

# Executes when the player decides to exit out of the loop
print("Thanks for playing!")
if playerScore > botScore:
  print(playerName + " wins!")
else:
  print("Computer wins!")
  

