##this file contains the code to read the blocks
# pass in a single block (single line of a single file)
from bitcoin import *
from genfunc import *
# Pass in the array of arrays with first element being the block number and the second being the raw block data
#
#

def compileBlock(raw):
	#code for breaking the block up goes here
	
	def loadBlock(rawString):
		blockarr = list(rawString[1][0])
		final = []
		blocklen = len(blockarr)

		#removes \n at the end
		blockarr.pop(blocklen - 1)
		final.append(rawString[0])
		final.append(blockarr)

		blocklen = len(blockarr)
		return final

	def toDict(array):
		output = {'_id': array[0], 'blen': array[1], 'bvers': array[2], 'bprev': array[3], 'bmerk': array[4],
		'btime': array[5], 'bdiff': array[6], 'bnonce': array[7], 'btxct': array[8], 'bhash': array[9]}

		return output

	# this section determines the length of the split - need to 
	# pass in length of sections
	def splitBlock(array):
		end = len(array[0]) - 1

		bnum = str(array[0][0])

		blen = array[1][0:8]
		bvers = array[1][8:16]
		bprev = array[1][16:80]
		bmerk = array[1][80:144]
		btime = array[1][144:152]
		bdiff = array[1][152:160]
		bnonce = array[1][160:168]
		btxct = array[1][168:170]
		bhash = array[1][170:]

		split = []
		split.append([bnum])
		split.append(blen)
		split.append(bvers)
		split.append(bprev)
		split.append(bmerk)
		split.append(btime)
		split.append(bdiff)
		split.append(bnonce)
		split.append(btxct)
		# always append bhash last
		split.append(bhash)

		return split

	def splitTx(tx):

		def findChecksig(array):
			checksig = array[-10:]
			return checksig


		def split88ac(string):
			array = string.split('ac00000000')
			new = []

			for entry in array:
				entry = entry + 'ac00000000'
				new.append(entry)

			new.pop(len(new) - 1)
			return new

		def getCoinbase(array):
			split = []
			new = array.pop(0)

			split.append([new])
			split.append(array)
			return split


		split = split88ac(tx)
		return split


	# Returns specific block
	#
	#
	loaded = loadBlock(raw)


	# Splits block into block headers and transactions
	#
	#
	splitblock = splitBlock(loaded)


	####################################################
	newarr = []
	key = 0
	lenSplit = len(splitblock) - 1
	#newarr.append(str(raw[0][0]))

	# while(key < lenSplit):
	# 	temp = toBigEndian(splitblock[key])
	# 	newarr.append(temp)
	# 	key += 1

	#####################################################


	# Turns the elements inside the array of arrays into strings, little-endian format
	# NOTE: You need to convert to big-endian before showing to end-users
	#
	stringedHash = toString(splitblock)


	dBlock = toDict(stringedHash)
	print(dBlock)


	##############################
	# * Returns a dictionary	
	# *						
	# *
	return dBlock


