# logic for any number system conversion to decimal

def conversiontodecimal(number, base):
	num = str(number)
	num_len = len(num)
	sum = 0
	for i in range(num_len):
		digit = number % 10
		number //= 10
		sum += digit * (base ** i)
	return sum


print(conversiontodecimal(121,8))

'''
NOTE: remain the logic for hex number system
'''