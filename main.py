#WELCOME TO THE ROCK PAPER SCISSORS GAME

#import random module
import random


while True:
	#collect input from users
	print("R= Random, P= Paper, S=Scissors")

	possible_action = ["R", "P", "S"]
	userInput = input("Enter your input: ")
	
	try:
		#selects an item for computer
		computer = random.choice(possible_action)
		#compare inputs
		if (UserInput == computer):
			print("There is no winner")
		elif(UserInput == R ):
			if (computer == "S"):
				print("Rock wins Scissors")
			else:
				print("Paper covers Rock")
		elif(UserInput == P ):
			if (computer == "R"):
				print("paper wins Rock")
			else:
				print("Scissors cuts Paper")
		elif(UserInput == S ):
			if (computer == "P"):
				print("Scissors cuts Paper")
			else:
				print("Rock wins Scissors")
	

	except:
		print("select a valid input")


	play_again = input("Do you want to play again: 'y' or 'n' ")
	if (play_again == "y"):
		break	
	elif (play_again == "n"):
		continue
	else:
		print("select 'y/n' only")
