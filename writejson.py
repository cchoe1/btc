import json
import datetime

def storeJson(dict):
	print(dict['_id'])
	filepath = '/media/calvin/hdd1/json/'
	filenum = str(dict['_id'])
	fileext = '.json'

	file = filepath + filenum + fileext

	with open(file, 'w') as fp:
		json.dump(dict, fp, indent=4)
	print("Successfully written to: ", file)

	
	