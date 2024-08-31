# logic for decimal to any number system conversion

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


print(decimal_conversion(4,5))
		