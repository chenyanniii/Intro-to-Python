## rock.py
## rock, paper, scissor game
## Human V.S. Computer
import random
computer_input = random.randint(1,3)
human_input= int(input("What do you choose? \n Input 1 for Rock \n Iput 2 for Paper \n Iput 3 or Scissors?"))

if human_input == computer_input:
	print("TIE")
elif human_input > computer_input:
	print("You win!")
elif human_input < computer_input:
	print("Sorry for your lost.")	
