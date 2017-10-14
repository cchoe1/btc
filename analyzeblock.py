import binascii
import hashlib
import datetime
import json
from genfunc import *


##########
# Pass this function a dictionary of the main, unaltered components of the block
# 	aka - first json files are used in this
# 
# This will then create the header, so it can be passed into a function to be hashed
# 
# All values this receives is in little endian, string format
#
# This function works on a block-by-block basis
#
# NOTE : You should always start this program at 1, because
# 	the genesis block is implied--there is no need to check it

def analysisForWeb(dinum):

	def returnDi(dinum):
		filepath = '/media/calvin/hdd/json/'
		filenum = str(dinum)
		fileext = '.json'

		file = filepath + filenum + fileext

		di = ''
		with open(file, 'r') as f:
			di = json.load(f)

		return di

	def createHeader(di):
		header = di["bvers"] + di['bprev'] + di['bmerk'] + di['btime'] + di['bdiff'] + di['bnonce']
		return header

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
		return finalLittle

	def createWebJson(curr, di):
		bnum = di['_id']
		bprev = di['bprev']
		thehash = curr


		verifyJson = ({"bline": bnum, 'bprev': bprev, "bcurr": thehash})
		return verifyJson

	####
	# Main logic begins here
	# 
	#

	di = returnDi(dinum)
	head = createHeader(di)
	hashed = hashBlock(head)


	

	jsonForWeb = createWebJson(hashed, di)
	print(jsonForWeb)


	return jsonForWeb