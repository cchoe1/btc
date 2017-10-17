from getwebjson import *
from writejson import *
import readtx

#webjson = analysisForWeb(1)

#print("The json = ", webjson['_id'])

#358379

# First P2SH transaction was on block 160720

x = 254713
y = x + 1

while(x < y):
	####
	#
	#
	#
	#line = readTree(x)



	####
	# getwebjson.py
	#
	#
	#print('-----------')
	webjson = analysisForWebB(x)
	webjson.update({'_id': str(x)})

	####
	# readtx.py
	#

	splitTx = readtx.splitTx(webjson['btx'])
	webjson.update({'btx': splitTx})
	z = x % 10

	if(z == 0):
		print(x)
	else:
		pass


	
	####
	# writejson.py
	# This is the final validated version of the blockchain data
	# Block order is verified and transactions are deserialized
	# Use these files to create the main transaction chain
	writeThirdJson(webjson, x)

	x += 1




