'''
Practical 05

Question-4: Develop a base method in Python which takes three arguments as text, text_base, output_base. This method is going to convert the text of the text_base into the output_base as mentioned in the parameter of the function.
	
'''

def base(text, text_base, output_base):
	decimal_text = conversiontodecimal(text, text_base)
	output_text = decimal_conversion(decimal_text, output_base)
	return output_text


# helping method to convert any number system to decimal number system
def conversiontodecimal(number, base):
	num = str(number)
	num_len = len(num)
	sum = 0
	for i in range(num_len):
		digit = number % 10
		number //= 10
		sum += digit * (base ** i)
	return sum

# helping method to convert decimal number system to any number system.
def decimal_conversion(number, base):
	temp = number
	converted_num = []
	while number >= base:
		number //= base # quotient
		remainder = temp % base
		temp = number
		converted_num.append(remainder)

	converted_num.append(number)
	converted_num.reverse()
	return converted_num


# checking logic of base method
print(base(11, 10, 8))