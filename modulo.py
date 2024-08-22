# Practical No. 04
# Q-3: Modulo operation using python

def modulo(numerator, denominator):
	# ZeroDivisionError: when denominator is 0
	if (denominator == 0):
		return -1

	# for normal modulus operation
	else:
		quotient = numerator // denominator
		remainder = numerator - (denominator * quotient)
		return remainder

	return remainder

#------ testing the functionality of modulo function ------
result = modulo(-10, 3)

if result == -1:
	print("Divide by zero exception")
else:
	print(result)




""" 
working of modulus
1) when we mod a number by smaller no it will divide and return the remainder
2) when we mod a number by greater no then it will return the nubmer itself as a return value.
3) here also divide by zero exception happen when we try to mod by 0
4) if number is exactly dividable the numerator by denominator then the function should return 0
5) else return the remainder
"""

'''
1] When small +denominator exactly divide the +numerator return 0 as a remaindar.
2] When small -denominator exactly divide the +numerator return 0 as a remaindar.
3]
4]
5]
'''
	