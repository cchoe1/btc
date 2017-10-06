##this file contains the code to read the blocks
# pass in a single block (single line of a single file)
from bitcoin import *

def compileBlock(raw):
	#code for breaking the block up goes here
	
	def loadBlock(rawString):
		blockarr = list(rawString)
		#removes \n at the end
		blocklen = len(blockarr)
		blockarr.pop(blocklen - 1)

		blocklen = len(blockarr)

		print('Length of block: ', blocklen, '\n')
		#print(blockarr)

		return blockarr

	def parseHash(hash):
		unhashed = deserialize(hash)
		print(unhashed)

	def toDict(array):
		output = {'_id': array[0], 'blen': array[1], 'bvers': array[2], 'bprev': array[3], 'bmerk': array[4],
		'btime': array[5], 'bdiff': array[6], 'bnonce': array[7], 'btxct': array[8], 'bhash': array[9]}
		return output

	# this section determines the length of the split - need to 
	# pass in length of sections
	def splitBlock(array):
		end = len(array) - 1

		blen = array[0:8]
		bvers = array[8:16]
		bprev = array[16:80]
		bmerk = array[80:144]
		btime = array[144:152]
		bdiff = array[152:160]
		bnonce = array[160:168]
		btxct = array[168:170]
		bhash = array[170:]

		split = []
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

	def toString(arr):
		string = ''.join(arr)
		return string

	
	def stringToList(string):
			output = string.split()
			return output

	#grouped = groupHex(arr)

	# accepts string, turns into byte pairs, 
	def toBigEndian(array):

		def listToPairs(listt):
			done = []
			final = []
			length = len(listt)
			key = 0

			while (key < length):
				done.append(listt[key])
				key += 1
				done.append(listt[key])
				key += 1
				final.append(done)
				done = []

			return final

		def reverseEndian(pair):
			done = []
			limit = len(pair) - 1
			final = []
			
			while (limit >= 0):
				step = 0
				array = []
	
				while (step <= 1):
					array.extend(pair[limit][step])
					step += 1
				limit -= 1
				final.append(array)
			done.extend(final)

			return done

		def toSingleArray(array):
			final = []
			for pair in array:
				key = 0
				while (key < 2):
					final.extend(pair[key])
					key += 1
			
			return final

		pair = listToPairs(array)
		revers = reverseEndian(pair)
		single = toSingleArray(revers)
		stringed = toString(single)

		return stringed

		

	#returns specific block
	loaded = loadBlock(raw[1][0])

	#splits block into block headers and transactions
	splitblock = splitBlock(loaded)

	####################################################
	newarr = []
	key = 0
	lenSplit = len(splitblock) - 1
	newarr.append(str(raw[0][0]))
	while(key < lenSplit):
		temp = toBigEndian(splitblock[key])
		newarr.append(temp)
		key += 1
	stringedHash = toString(splitblock[lenSplit])

	newarr.append(stringedHash)

	#**create dictionary after converting to big endian format
	dBlock = toDict(newarr)


	# bLength = toBigEndian(dBlock['blen'])



	# txString = toString(dBlock['bhash'])
	# txSplit = splitTx(txString)
	# dBlock['bhash'] = txSplit

	return dBlock

			
	#return converted

