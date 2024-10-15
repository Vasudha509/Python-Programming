# guess the number - game DONE

from random import randint

def guess_the_number():
	sn = initialization()
	status = start_game(sn)
	stop_game(status)


# helper function to initialize the code
def initialization():
	print("-----Welcome to the Game-----")
	sn = randint(1, 10)
	return sn

# helper function to start the game
def start_game(sn):
	guess = int(input("guess number between 1 to 10 : "))
	print("The number is - ", sn)
	return guess == sn

# helper function to stop the game
def stop_game(status):
	if status:
		print("Congratulation, you Win the game. ")
	else:
		print("Sorry, but you Lossed")

# checking functionality of the game
guess_the_number()