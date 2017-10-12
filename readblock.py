##this file contains the code to read the blocks
# pass in a single block (single line of a single file)
from bitcoin import *
from genfunc import *
# Pass in the array of arrays with first element being the block number and the second being the raw block data
# Reads from INT1 files - receives little-end values
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

	


	# Returns specific block
	#
	#
	loaded = loadBlock(raw)


	# Splits block into block headers and transactions
	#
	#
	splitblock = splitBlock(loaded)


	# Turns the elements inside the array of arrays into strings, little-endian format
	# NOTE: You need to convert to big-endian before showing to end-users
	#
	stringedHash = toString(splitblock)


	dBlock = toDict(stringedHash)


	##############################
	# * Returns a dictionary	
	# *						
	# *
	return dBlock


