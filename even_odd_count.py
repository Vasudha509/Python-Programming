# Program to get the count of even odd numbers from the give list. Try different different methods and find which approach is most efficient. Also find the required time for each approach.

from time import time
def get_even_odd_count():
	before_time, after_time = 0, 0
	required_time1, required_time2, required_time3, required_time4 = 0, 0, 0, 0

	list_number_list = [[1,2,3,4,6,3,6,65,33,4,54,92,58,232,154,232,78,454,236,58,8,87,123,568,675],
				[1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
				[5, 10, 15, 20, 25, 30, 35, 40, 45, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100],
				[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500],
				[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610,3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 987],
				[2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768],
				[50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900],
				[3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51, 54],
				[1, 4, 9, 16, 25, 36, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105,49, 64, 81, 100, 121, 144, 169, 196, 225],
				[10, 30, 50, 70, 90, 110, 130, 150, 170, 190, 210, 230, 250, 270, 290],
				[11, 22, 33, 44, 55, 66, 77, 88, 99, 110, 121, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105,132, 143, 154, 165],
				[12, 24, 36, 48, 60, 72, 84, 96, 108, 120, 132, 144, 156, 168,3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 180],
				[101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118],
				[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 55, 60, 65, 70, 75, 80, 85],
				[1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 1203, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105,],
				[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 47],
				[12, 7, 5, 10, 14, 20, 21, 34, 45, 56, 67, 78, 89, 90, 100, 102, 115, 120, 125, 130],
				[1, 3, 4, 6, 7, 9, 10, 11, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 13, 15, 17, 18, 20, 22, 24, 26, 28, 30, 32, 34],
				[100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000],
				[5, 15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165, 175, 185, 195],
				[8, 9, 12, 15, 16, 18, 22, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 25, 28, 32, 34, 36, 40, 42, 44, 46, 50, 52, 56, 58],
				[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28,3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 30, 32, 34, 36, 38],
				[17, 23, 29, 31,3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103],
				[6, 11, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105,13, 15, 19, 21, 25, 27, 33, 35, 37, 41, 43, 47, 49, 53, 59, 61, 67, 71],
				[4, 12, 18, 24, 30, 42, 48, 54, 60, 72, 84, 90, 96, 100, 110, 120, 130, 140, 150, 160],
				[9, 14,3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105, 17, 22, 26, 28, 33, 38, 41, 46, 52, 57, 60, 63, 68, 72, 79, 81, 87, 91]]
	
	
	for list_number in list_number_list:
		# Checking performance of 1st approach
		before_time = time()
		even_count, odd_count = approach1(list_number)
		after_time = time()
		required_time1 += abs(before_time - after_time)

	for list_number in list_number_list:
		# Checking performance of 2nd approach
		before_time = time()
		even_count, odd_count = approach2(list_number)
		after_time = time()
		required_time2 += abs(before_time - after_time)
		
	for list_number in list_number_list:
		# Checking performance of 3rd approach
		before_time = time()
		even_count, odd_count = approach3(list_number)
		after_time = time()
		required_time3 += abs(before_time - after_time)
	
	for list_number in list_number_list:	
		# Checking performance of 4th approach
		before_time = time()
		even_count, odd_count = approach4(list_number)
		after_time = time()
		required_time4 += abs(before_time - after_time)
		

	# average time
	avg_time1 = required_time1 // len(list_number_list)
	avg_time2 = required_time2 // len(list_number_list)
	avg_time3 = required_time3 // len(list_number_list)
	avg_time4 = required_time4 // len(list_number_list)

	# Displaying the result p
	print("Average time taken by approach 1: {:.6f} seconds".format(avg_time1))
	print("Average time taken by approach 2: {:.6f} seconds".format(avg_time2))
	print("Average time taken by approach 3: {:.6f} seconds".format(avg_time3))
	print("Average time taken by approach 4: {:.6f} seconds".format(avg_time4))

	# Finding most efficient approach
	eff_app = min(avg_time1, avg_time2, avg_time3, avg_time4)
	print("\nEfficient Approach time required : ", eff_app)

# Approach 1: Normal way
def approach1(l):
	even_count, odd_count = 0, 0
	
	for ele in l:
		if ele % 2 == 0:
			even_count += 1
		else:
			odd_count += 1

	return even_count, odd_count


# Approach 2: 
def approach2(l):
	even_count, odd_count = 0, 0
	
	for ele in l:
		if ele % 2:
			odd_count += 1
		else:
			even_count += 1

	return even_count, odd_count


# Approach 3:
def approach3(l):
	even_count, odd_count = 0, 0
	
	for ele in l:
		t = ele % 2
		odd_count += t
		even_count = 1 - t

	return even_count, odd_count


# Approach 4:
def approach4(l):
	even_count, odd_count = 0, 0
	
	for ele in l:
		if ele & 1: # check last  bit for odd/even
			odd_count += 1
		else:
			even_count += 1

	return even_count, odd_count


get_even_odd_count()