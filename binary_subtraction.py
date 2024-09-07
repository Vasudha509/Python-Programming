# Program to perform binary subtraction

def binary_subtraction(num1, num2):
	result_list = []
	flag = 0

	# For loop to iterate all the digits of the number string
	for i in range(len(num1)):
		digit_str1 = num1[len(num1)-i-1]
		digit_str2 = num2[len(num2)-i-1]

		digit_int1 = convert_str_to_int(digit_str1)
		digit_int2 = convert_str_to_int(digit_str2)
		
		
		if flag:
			digit_int2 = 1
			flag = 0

		if digit_int1 == 0 and digit_int2 == 0:
			result = digit_int1 ^ digit_int2
			result_list.append(result)

		elif digit_int1 == 0 and digit_int2 == 1:
			result = digit_int1 ^ digit_int2
			result_list.append(result)
			flag = 1

		elif digit_int1 == 1 and digit_int2 == 0:
			result = digit_int1 ^ digit_int2
			result_list.append(result)
			
		elif digit_int1 == 1 and digit_int2 == 1:
			result = digit_int1 ^ digit_int2
			result_list.append(result)

	result_list.reverse()
	result = convert_list_to_int(result_list)
	return result

# Method to convert the string to integer
def convert_str_to_int(digit):
	return ord(digit) - 48

# Method to convert the list to integer
def convert_list_to_int(digit_list):
	result = 0
	for num in digit_list:
		result = result * 10 + num

	return result

# testing the functionality of binary subtraction 
# case 1: '10101' - '01001' = 01100
num1 = '10101'
num2 = '01001'
print("Case 1: ", binary_subtraction(num1, num2))

# testing the functionality of binary subtraction 
# case 2: '110' - '011' = 101
num1 = '110'
num2 = '011'
print("Case 2: ", binary_subtraction(num1, num2))

# testing the functionality of binary subtraction 
# case 3: '10000' - '00001' = 01111
num1 = '10000'
num2 = '00001'
print("Case 3: ", binary_subtraction(num1, num2))




