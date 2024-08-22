'''
Practical No. 05:

You need to create a change_case method that takes 2 arguments:

1. str: The input string
2. style: A string representing the desired case transformation style

There are 4 options for the style parameter:

- "c": Converts the entire string to uppercase.
- "s": Converts the entire string to lowercase.
- "r": Reverses the case of each character (i.e., if the character is lowercase, it converts it to uppercase, and vice versa).
- "u": If the first letter is uppercase, the string should alternate between lowercase and uppercase (e.g., "HeLLo"). If the first letter is lowercase, it should alternate between uppercase and lowercase (e.g., "hElLo").
'''

# Main Method defination
def change_case(string, style):
	converted_string = ''

	if style == 'c':
		converted_string = uppercase(string)
			
	elif style == 's':
		converted_string = lowercase(string)
	
	elif style == 'r':
		converted_string = reverse_case(string)
	
	elif style == 'u':
		converted_string = alter_case(string)
			
	else:
		return -1

	return converted_string


# Helping Method: To convert into Uppercase
def uppercase(string):
	uppercase_string = ''
	uppercase_list = []

	list_str = []
	list_str.extend(string)

	for i in range(len(list_str)):
		ascii_value = ord(list_str[i])
		
		if ascii_value >= 65 and ascii_value <= 90:
			uppercase_list.append(list_str[i])

		elif ascii_value >= 97 and ascii_value <= 122:
			ascii_value -= 32
			uppercase_list.append(chr(ascii_value))
		else:
			return -1

	uppercase_string = ''.join(uppercase_list)	
	return uppercase_string


# Helping Method: To convert into lowercase
def lowercase(string):
	lowercase_string = ''
	lowercase_list = []

	list_str = []
	list_str.extend(string)

	for i in range(len(list_str)):
		ascii_value = ord(list_str[i])
		
		if ascii_value >= 97 and ascii_value <= 122:
			lowercase_list.append(list_str[i])

		elif ascii_value >= 65 and ascii_value <= 90:
			ascii_value += 32
			lowercase_list.append(chr(ascii_value))
		else:
			return -1

	lowercase_string = ''.join(lowercase_list)	
	return lowercase_string


# Helping Method: To convert into reverse case
def reverse_case(string):
	reversecase_string = ''
	reversecase_list = []

	list_str = []
	list_str.extend(string)

	for i in range(len(list_str)):
		ascii_value = ord(list_str[i])
		
		if ascii_value >= 65 and ascii_value <= 90:
			ascii_value += 32
			reversecase_list.append(chr(ascii_value))

		elif ascii_value >= 97 and ascii_value <= 122:
			ascii_value -= 32
			reversecase_list.append(chr(ascii_value))
		else:
			return -1

	reversecase_string = ''.join(reversecase_list)	

	return reversecase_string


# Helping Method: alteration between uppercase and lowercase
def alter_case(string):
	alter_string = ''
	
	# Iterate through the string and apply the "hElLo" pattern
	for i, char in enumerate(string):
		if i % 2 == 0:
			alter_string += char.lower()
		else:
			alter_string += char.upper()
    
	return alter_string


# Testing the functionality
print(change_case('Vasudha', 'c'))
print(change_case('Vasudha', 's'))
print(change_case('VasUdhA', 'r'))
print(change_case('VasUdhA', 'u'))