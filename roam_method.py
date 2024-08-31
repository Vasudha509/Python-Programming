'''
Practical 05

Question-3: Develop a roam method in Python which takes two arguments as text and text_base and convert it into the roam number system.

'''

def roam(text, text_base):
	decimal = conversiontodecimal(text, text_base)
	roam_value = equivalent_roam(decimal)
	return roam_value

def conversiontodecimal(number, base):
	num = str(number)
	num_len = len(num)
	sum = 0
	for i in range(num_len):
		digit = number % 10
		number //= 10
		sum += digit * (base ** i)
	return sum

def equivalent_roam(num):
	m = ["", "M", "MM", "MMM"]
	c = ["", "C", "CC", "CCC", "CD", "D","DC", "DCC", "DCCC", "CM "]
	x = ["", "X", "XX", "XXX", "XL", "L","LX", "LXX", "LXXX", "XC"]
	i = ["", "I", "II", "III", "IV", "V","VI", "VII", "VIII", "IX"]

	# Converting to roman
	thousands = m[num // 1000]
	hundreds = c[(num % 1000) // 100]
	tens = x[(num % 100) // 10]
	ones = i[num % 10]

	ans = (thousands + hundreds + tens + ones)

	return ans

print(roam(1, 10))	