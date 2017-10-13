import binascii
import hashlib
import datetime
import json
from readfile import *
from genfunc import *
from bitcoin import *


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

def analysisForWebB(dinum):
	line = readTree(dinum)
	
	def getTxArr(txArr):
		print("Test")

	def returnDi(dinum):
		filepath = '/media/calvin/hdd1/json/'
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


	def getTimeReadable(di):
		time = di["btime"]
		timeRev = toBigEndian(time)

		readable = datetime.datetime.fromtimestamp( int(timeRev, 16) ).strftime('%Y-%m-%d %H:%M:%S')
		return readable

	# This will create the final dictionary that gets returned from this functions
	# Accepts little-end values
	# Returns array
	def splitTx(tx):

		def getCoinbase(array):
			split = []
			inc = 0

			print(array)
			new = array.split('ac00000000', 1)
			new[0] = new[0] + 'ac00000000'
			print('Split successful', inc)
			return new

		def split88ac(string):
			inc = 0
			coinbase = getCoinbase(string)
			array = coinbase[1].split('88ac00000000')
			new = []
			new.append(coinbase[0])

			for entry in array:
				entry = entry + '88ac00000000'
				new.append(entry)

			new = new[:-1]
			return new

		split = split88ac(tx)
		return split
	####
	# Pass in an array of the transactions
	#
	def readTx(arr):
		new = []
		inc = 0
		for tx in arr:
			try:
				temp = deserialize(tx)
				new.append(temp)
				print("Successfully read tx", inc)
				inc += 1
				
			except (IndexError, binascii.Error):
				print("Error reading tx", tx)
				pass
		return new

	def createWebJson(arr, di, dinum):
		nextNum = dinum + 1
		nextLine = readTree(nextNum)
		nextLineHash = nextLine[1]

		# nextdi = returnDi(nextLineIndex)
		# nexthead = createHeader(nextdi)
		# nexthash = hashBlock(nexthead)
		btx = splitTx(di['bhash'])
		btxRead = readTx(btx)

		bnum = di['_id']
		bvers = toBigEndian(di['bvers'])
		bprev = toBigEndian(di['bprev'])
		bmerk = toBigEndian(di['bmerk'])
		btime = toBigEndian(di['btime'])
		bdiff = toBigEndian(di['bdiff'])
		bnonce = toBigEndian(di['bnonce'])
		bhash = toBigEndian(arr[1])
		btimer = arr[2]
		btxct = toBigEndian(di['btxct'])
		bnext = toBigEndian(nextLineHash)
		blen = toBigEndian(di['blen'])

		webJson = ({'blen': blen, "bline": bnum, 'btxct': btxct, 'bnext': bnext, "bhash": bhash, "btimer": btimer,
			"bhead": {"bvers": bvers, 'bprev': bprev, 'bmerk': bmerk, 'btime': btime, 'bdiff': bdiff, 'bnonce': bnonce},})

		txArr = []

		incr = 0
		for tx in btxRead:
			txArr.append([{'btxraw': btx[incr], 'btxinfo': tx}])
			incr += 1


		webJson.update({'btx': txArr })

		####
		# This final object that is passed is what will be displayed
		# Make all edits before this returns
		#
		return webJson

	####
	# Main logic begins here
	# 
	#

	temparr = []

	di = returnDi(line[0])
	head = createHeader(di)
	hashed = hashBlock(head)
	time = getTimeReadable(di)

	temparr.append(head)
	temparr.append(hashed)
	temparr.append(time)

	

	jsonForWeb = createWebJson(temparr, di, int(dinum))


	return jsonForWeb
