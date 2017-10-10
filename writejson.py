import json
import datetime

####
# Creates the first json file - unordered list of raw hex
# Called by controller.py
# 
# Relies on first intermediate files (.txt) to run
#
def writeFirstJson(dict):
	filepath = '/media/calvin/hdd1/json/'
	filenum = str(dict['_id'])
	fileext = '.json'

	file = filepath + filenum + fileext

	with open(file, 'w') as fp:
		json.dump(dict, fp, indent=4)
	print("Successfully written to: ", file)


####
# Creates second JSON file - unordered list of block line #, previous block, and current block
# This JSON file is used to write to the main ledger and create an organized block chain
# 
# Called by analyzecontroller.py
#
# Relies on firstJson output
#
def writeSecJson(di):
	filepath = '/media/calvin/hdd1/firstTree/'
	filenum = str(di['bline'])
	fileext = '.json'
	file = filepath + filenum + fileext
	
	with open(file, 'w') as fp:
		json.dump(di, fp, indent=4)
	print("Finished writing file to ", file)


####
# Relies on the maintree.txt file - writetree.py must be updated
#
#
def writeThirdJson(dict, start):
	filepath = '/media/calvin/hdd1/webjson/'
	filenum = str(start)
	fileext = '.json'
	
	file = filepath + filenum + fileext

	with open(file, 'w') as fp:
		json.dump(dict, fp, indent=4)
	print("Finished writing to file: ", file)