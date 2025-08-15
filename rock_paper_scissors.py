import random
choices = ["rock", "paper", "scissors"]
playerScore = 0
botScore = 0
playerName = input("What is your name?")

while True:
  playerChoice = input("Welcome to Rock, Paper, Scissors! Enter a choice (or 'quit') to exit").lower()
  if playerChoice == "quit":
    break
  if playerChoice not in choices:
    print("Invalid selection. Try again.")
    continue
  computer = random.choice(choices)
  print("Computer chose " + computer)

  if playerChoice == computer:
    print("It's a tie!")
  elif playerChoice == "rock" and computer == "scissors" or playerChoice == "paper" and computer == "rock" or playerChoice == "scissors" and computer == "paper":
    print("You win!")
    playerScore += 1
    print("Player: " + str(playerScore) + " - " + "Bot: " + str(botScore))
  else:
    print("Computer wins!")
    botScore += 1
    print("Player: " + str(playerScore) + " - " + "Bot: " + str(botScore))
  
print("Thanks for playing!")
if playerScore > botScore:
  print(playerName + " wins!")
else:
  print("Computer wins!")
  
