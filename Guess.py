### "Guess-the-Number"
##########################################

# 1. Computer pick a random number
# 2. Player input a number
# 3. Compare computer number with player number

##############################################
# 1. Computer pick a random number 
#	- pick a random number between as computer number
# 2. Player input a number
#	- the player input a number
# 3. Compare computer number with player number: 
# 	- compare player number with computer number
#		-if player number is equal to computer number
#		-if player number is greater than computer number, display "too high", input another\
#			player number
#		-if player number is less than computer number, display "too low", input another\
#			player number
#		

################################################

import random
computer_pick = random.randint(1,1000)

guess_input = input("What number do you guess?")
guess = int(guess_input)

if guess == computer_pick:
		print("Congratulations! You got the right number!")

while guess != computer_pick:
		if guess > computer_pick:
				guess_input = input("Too high! Try a smaller number. What do you get this time?")
				guess = int(guess_input)

		elif guess < computer_pick:
				guess_input = input("Too low! Try a larger number. What do you get this time?")
				guess = int(guess_input)


print("The computer pick number is " + str(computer_pick) + ".")
print("Congratulations! You got the right number!")
