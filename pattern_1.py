# Practical No. 04
# Q-1: Design the given pattern

def pattern_1(num):
	rows = num + 1
	cols = (2 * num) + 1

	# logic for the upper triangle
	for i in range(1, rows):
		for j in range(1,cols+1):
			if i + j == num + 2 or j - i == num:
				print("+", end="")
			else:
				print(" ", end="")
		print()


	# logic for the lower triangle
	for i in range(1, rows):
		for j in range(1, cols+1):
			if i == j or i + j == 2 * rows:
				print("+", end="")
			else:
				print(" ", end="")
		print()

	print(" "*(num-1), "-")


pattern_1(1)