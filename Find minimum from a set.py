import numpy as np
#Any random values are entered into the dictionary
a_dict = {12,32,45,85,34,94,15,28,43}
#The dictionary can be converted into list by using the function list()
a_list = list(a_dict)
#Converting the list into numpy array
a_list_arr = np.array(a_list)
#The function min() finds the minimum value of the array, a_list_arr
print((a_list_arr).min())
