# Program to perform decimal subtraction in python

def decimal_subtraction(num1, num2):
	result_list = []

	# For loop to iterate all the digits of the number string
	for i in range(len(num1)):
		digit_str1 = num1[len(num1)-i-1]
		digit_str2 = num2[len(num2)-i-1]

		digit_int1 = convert_str_to_int(digit_str1)
		digit_int2 = convert_str_to_int(digit_str2)
		
		result = digit_int1 - digit_int2
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

# testing the functionality of decimal subtraction 

# case 1: '94' - '23' = 71
num1 = '94'
num2 = '23'
print("Case 1: ", decimal_subtraction(num1, num2))

# case 2: '23' -'94' = -71
num1 = '23'
num2 = '94'
print("Case 2: ",decimal_subtraction(num1, num2))

# case 3: '2134' -'0122' = 2012 
num1 = '2134'
num2 = '0122'
print("Case 3: ",decimal_subtraction(num1, num2))

# case 4: '342' -'123' = 219 
num1 = '342'
num2 = '123'
print("Case 4: ",decimal_subtraction(num1, num2))

# case 5: '124' -'281' = -157 
num1 = '124'
num2 = '281'
print("Case 5: ",decimal_subtraction(num1, num2))


