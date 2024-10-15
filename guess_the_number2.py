# guess the number and win the prises - game

'''
The given game is going to give the rewards to the gamer as per the the attempts and how well it's played. If in first attempts its win 5x, 2nd attempts 4x, 3rd attempts 3x and if in 4th attempts 2x and if in 5 attempts then 1x. And also providing the hint where the number. Their is 5 hint. 1st - exact number, 2nd - number is to less, 3rd number is less, 4th number is to big, 5th number is big.
'''

from random import randint

def guess_the_number():
	sn, st, en = initialization()
	status = start_game(sn, st, en)
	stop_game(status)


# helper function to initialize the game.
def initialization():
	print("\n\n----- Welcome to the Game -----")

	rewards = {1:1, 2:2, 3:3, 4:4, 5:5}

	print("\n\nRewards of the game\n")
	print(" 1st Attempt : 5X\n",
	      "2nd Attempt : 4X\n",
	      "3rd Attempt : 3X\n",
	      "4th Attempt : 2X\n",
	      "5th Attempt : 1X\n")

	print("\nEnter the level of difficult ")
	print("\n1.Easy\n2.Medium \n3.Hard\n")
	choice = int(input("Enter the choice - "))
	
	start, end = 0, 0
	
	# setting the level of difficulty
	if choice == 1:
		start = 0
		end = 10

	elif choice == 2:
		start = 0
		end = 20

	else:
		start = 0
		end = 30
	
	# generating the numbers between start and end using built in randint function. 	
	sn = randint(start, end)
	return sn, start, end

# helper function to start the game.
def start_game(sn, st, en):
	rewards = 0
	for attempt in range(1,6):
		print(f"\nAttempts: {attempt}")
		guess = int(input(f"guess number between {st} to {en} : "))
		rewards = guess


		if guess == sn:
			if attempt == 1:
				rewards *= 5 

			elif attempt == 2:
				rewards *= 4

			elif attempt == 3:
				rewards *= 3

			elif attempt == 4:
				rewards *= 2

			elif attempt == 5:
				rewards *= 1

			print("The number is - ", sn)

			print(f"Reward : {rewards}")
			return True

	else:
		print("\nThe number is - ", sn)
		return False
	
# helper function to stop the game.
def stop_game(status):
	if status:
		print("\nCongratulation you Win the game.")
	else:
		print("\nSorry, try next time")

guess_the_number()