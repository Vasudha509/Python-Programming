'''
Python program to find second smallest and second largest value from the list. Here, list contains may be int, float, string, list, tuple, set, dict, etc. Only number type of object is considered.
'''

def get_SL_SS(l):
	# calling method to convert the list of objects to a list of numbers
	list_number = list_object_number(l)
	
	# sorting the list of numbers
	num_list = sort_list(list_number)

	if len(num_list) < 2:
		return "Error: Not enough numeric values to find second largest and second smallest."

	second_large_num = get_second_largest(num_list)
	second_small_num = get_second_smallest(num_list)

	return second_large_num, second_small_num

# Helper method to convert list of objects to list of number
def list_object_number(l):
	list_number = [] 

	# Iterate the list to find what kind of objects are there.
	for obj in l:
		if isinstance(obj, (int, float)):
			list_number.append(obj)	# append number types
		
		# when object is a list
		elif isinstance(obj, list):
			list_number.extend(list_object_number(obj))

		# when object is tuple or set
		elif isinstance(obj, (tuple, set)):
			list_number.extend(list_object_number(list(obj)))

		# when object is dictionary (keys and values both are processed)
		elif isinstance(obj, dict):
			list_number.extend(list_object_number(list(obj.keys())))
			list_number.extend(list_object_number(list(obj.values())))

	return list_number


# Helper method to sort the list of numbers
def sort_list(l):
	l.sort()
	return l	


# Helper method to find the second largest element from the list
def get_second_largest(element):
	return element[-2]


# Helper method to find the second smallest element from the list			
def get_second_smallest(element):
	return element[1]
	
list_object = [-1, -2, 3, ("vasudha", 4, 5, 98), {1:10, 2:20}, {43, 21, 56}, "SGGS", [2, 3, 4]]
print(get_SL_SS(list_object))

