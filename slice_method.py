'''
Practical 05

Question-1: Develop a slice method in Python which takes two arguments as object and slicing parameter and work like a slice operator in Python. Objest might be string, tuple, list in Python. Slicing Parameter is list might be empty, or at most 3 values.

Working of Slice operator in Python:
[start_from : end_at : steps]	
'''

def slice(object, slicing_parameter):
 
	''' --------------------- logic of slice on string object  --------------------- '''

	if isinstance(object, str):
		# when slicing parameter is empty return the whole string as it is.
		if len(slicing_parameter) == 0:
			return object

		# when slicing paramenter is one then it is a end parameter, return the string upto that parameter
		elif len(slicing_parameter) == 1:
			string_upto = []
			end = slicing_parameter[0]
			for i in range(end):
				string_upto.append(object[i])	
			return ''.join(string_upto)
			 
				
		# when slicing parameters are two then first one will acts like a starting index and second one acts like a ending index
		elif len(slicing_parameter) == 2:
			string_start_end = []
			start_from = slicing_parameter[0]
			end_upto = slicing_parameter[1]
			for i in range(start_from, end_upto):
				string_start_end.append(object[i])
			return ''.join(string_start_end)
			 

		# when slicing parameters are three then third one will acts like increment parameter
		elif len(slicing_parameter) == 3:
			string_start_end_incr = []
			start_from = slicing_parameter[0]
			end_upto = slicing_parameter[1]
			incr = slicing_parameter[2]
			for i in range(start_from, end_upto, incr):
				string_start_end_incr.append(object[i])
			return ''.join(string_start_end_incr)

	'''end of string logic'''



	
	'''--------------------- logic of slice on list object  ---------------------'''
	if isinstance(object, list):
		# when slicing_parameter is empty - return the whole list as it is
		if len(slicing_parameter) == 0:
			return object

		# when slicing_parameter is one - first param acts like a end of the list
		if len(slicing_parameter) == 1:
			return_list = []
			end_upto = slicing_parameter[0]
			for i in range(end_upto):
				return_list.append(object[i])
			return return_list


		# when slicing_parameter is two - second param acts like a start of the list
		if len(slicing_parameter) == 2:
			return_list = []
			start_from = slicing_parameter[0]
			end_upto = slicing_parameter[1]
			for i in range(start_from, end_upto):
				return_list.append(object[i])
			return return_list


		# when slicing_parameter is three - third param acts like a increment of the list
		if len(slicing_parameter) == 3:
			return_list = []
			start_from = slicing_parameter[0]
			end_upto = slicing_parameter[1]
			incr_by = slicing_parameter[2]
			for i in range(start_from, end_upto, incr_by):
				return_list.append(object[i])
			return return_list


	'''end of list logic'''



	'''--------------------- logic of slice on tuple object  ---------------------'''
	if isinstance(object, tuple):
		# when slicing_parameter is empty - return the whole tuple as it is
		if len(slicing_parameter) == 0:
			return object


		# when slicing_parameter is one - first param acts like a start of the list
		elif len(slicing_parameter) == 1:
			return_tuple_list = []
			end_upto = slicing_parameter[0]
			for i in range(end_upto):
				return_tuple_list.append(object[i])
			return tuple(return_tuple_list)


		# when slicing_parameter is two - second param acts like a end of the list
		elif len(slicing_parameter) == 2:
			return_tuple_list = []
			start_from = slicing_parameter[0]
			end_upto = slicing_parameter[1]
			for i in range(start_from, end_upto):
				return_tuple_list.append(object[i])
			return tuple(return_tuple_list)

		# when slicing_parameter is three - three param acts like a incr of the list
		elif len(slicing_parameter) == 3:
			return_tuple_list = []
			start_from = slicing_parameter[0]
			end_upto = slicing_parameter[1]
			incr_by = slicing_parameter[2]
			for i in range(start_from, end_upto, incr_by):
				return_tuple_list.append(object[i])
			return tuple(return_tuple_list) 
		
			
	'''end of tuple logic'''




'''
# checking the functionality of string object
object = "vasudha"
slicing_parameter = [0,7]
print(slice(object, slicing_parameter))
'''

'''
# checking the functionality of list object
object = [1,2,3,4,5,6,7,8,9,0]
slicing_parameter = [9,0,-1]
print(slice(object, slicing_parameter))
'''

# checking the functionality of tuple object
object = (1,2,3,4,5,6,7,8,9)
slicing_parameter = [1,9,2]
print(slice(object, slicing_parameter))
