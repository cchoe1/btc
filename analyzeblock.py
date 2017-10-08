import binascii
import hashlib
import datetime
import json
from genfunc import *

##########
# Pass this function a dictionary of the main, unaltered components of the block
# This will then create the header, so it can be passed into a function to be hashed
# 
# All values this receives is in little endian, string format
#
# This function works on a block-by-block basis
#

def analysisForWeb(di):

	def createHeader(di):
		header = di["bvers"] + di['bprev'] + di['bmerk'] + di['btime'] + di['bdiff'] + di['bnonce']
		return header

	####
	# Here we create a string of the block header--passed in as little endian format.
	# All hashes done by the Bitcoin-qt is done with little-endian formatted hex strings
	#
	blockHeader = createHeader(di)
	
	####
	# This function will accept a *string*, consisting of the *block header* { [block version] , [prev block] ,
	#	 [merkle root] , [timestamp] , [bits] , [nonce] }
	#
	# Then it will be encoded into bytes and converted to binary with binascii
	#
	# Finally, it will be hashed with SHA256(SHA256()) and converted back to hexadecimal with binascii
	def hashBlock(header):
		temp = header.encode('utf-8')
		header_bin = binascii.a2b_hex(temp)
		hashed = hashlib.sha256(hashlib.sha256(header_bin).digest()).digest()
		
		little = binascii.b2a_hex(hashed)
		big = binascii.b2a_hex(hashed[::-1])

		####
		# Two final outputs, either big or little
		# Potentially: create an option to choose endianness
		#
		finalLittle = little.decode('utf-8')
		finalBig = big.decode('utf-8')
		return finalBig
	

	def getTimeReadable(di):
		time = di["btime"]
		timeRev = toBigEndian(time)


		readable = datetime.datetime.fromtimestamp( int(timeRev, 16) ).strftime('%Y-%m-%d %H:%M:%S')
		print(readable)
		return readable

	def writeFirstJson(di, current):
		filepath = '/media/calvin/hdd1/firstTree/'
		filenum = str(di['_id'])
		fileext = '.json'
		file = filepath + filenum + fileext

		firstTree = {'bline': di['_id'], 'bprev': di['bprev'], 'bcurr': current}
		
		with open(file, 'w') as fp:
			json.dump(firstTree, fp, indent=4)

		print("Finished writing file to ", file)

	head = createHeader(di)
	hashed = hashBlock(head)
	time = getTimeReadable(di)

	writeFirstJson(di, hashed)

	print("Current block hash: ", hashed)
	print("This block was mined on: ", time)

	####
	# End of first half of analysisForWeb()
	# 
	# Now we must take the first JSON file and create the main tree 
	# 	and organize the blocks into the proper order
	# 
	# Create a second JSON file that uses the first to determine the proper
	# 	order based on the previous block hash and the current hash
	#



		