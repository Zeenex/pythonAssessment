

import sys
import json
import pprint

def createArraySchema(array_val):

	## get type of array_val
	arr_type = type(array_val)

	## check type
	if arr_type is dict:
		return createSchema(array_val)
	elif arr_type is int or arr_type is long or arr_type is float:
		return "Number"
	elif arr_type is bool:
		return "Boolean"
	elif arr_type is str or arr_type is unicode:
		return "String"

def createSchema(doc):

	## create object schema
	schema = {}

	## loop through keys
	for key in doc:
		## get key type
		key_type = type(doc[key])

		## change key from unicode to string
		key = str(key)

		## Check which type this is
		if key_type is int or key_type is long or key_type is float:
			schema[key] = "Number"
		elif key_type is bool:
			schema[key] = "Boolean"
		elif key_type is str or key_type is unicode:
			schema[key] = "String"
		elif key_type is list:
			## create array and add to current schema
			schema[key] = [createArraySchema(doc[key][0])]
		elif key_type is dict:
			## create object and add to current schema
			schema[key] = createSchema(doc[key])
		else:
			print ("unknown type:", key_type)

	## return fnished schema
	return schema


def getSchema(file_name):

	with open(file_name) as data_file:    
		doc = json.loads(data_file.read()) 
		return createSchema(doc)

if __name__ == "__main__":
	file_name = ""

	## test if file name given in command line
	if len(sys.argv) == 2:
		## grab from command line
		file_name = sys.argv[1]
	else:
		## Get file from user
		file_name = raw_input("Please enter file name: ")

	print (json.dumps(getSchema(file_name)))
