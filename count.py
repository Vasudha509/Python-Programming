# Practical No. 04
# Q-4: Count function to count the number of substring present in the given string

def count(string, substring, flag):
	count = 0
	start = 0

	# logic when string is empty
	if string == '':
		return -1

	# logic when sub string is not provided
	if substring == '':
		return string

	# Main logic 
	while True:
		start = string.find(substring, start)
	
		if start == -1:
			break

		count += 1

		# if overlapping is allowed, move the start by 1 character, else move past the substring
		start += 1 if flag else len(substring)

	return count


# Checking the logic 
result = count("sgggggs", "gg", True)

if result == -1:
	print("String Not Found Error")
else:
	print("count : ", result)



'''
1) count function is going to take 3 arguments
	i] first argument will take string
	ii] second argument will take substring
	iii] and third will be the flag which going to set the way to count the will count the string

2) flag: 
	- set to true
	If flag set to true it means we can overlap the string
	- set to false
	If flag set to false it means we can't overlap the string. It will work exactly as given built in function of the string 'count' function.

3) finally return the count of the substring present in the string.

4) take multiple example and try to understand the logic and the concept of the problem statement

5) try for empty string too. 
6) if user not provide substring then - return the all string as given


'''