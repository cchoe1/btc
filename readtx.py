from bitcoin import *

def splitTx(tx):

	def getCoinbase(array):
		split = []
		####
		# Gets the first transaction by splitting by the checksum + locktime
		#
		new = array.split('ac00000000', 1)
		new[0] = new[0] + 'ac00000000'

		####
		# This will remove a stray entry on the end if the block only contains 1 transaction
		#
		if(new[1] == ''):
			removed = new.pop()
		return new

	def split88ac(string):
		coinbase = getCoinbase(string)

		try:
			coinbase[1] = coinbase[1].replace('88ac0000000001', '88ac00000000|01')
			coinbase[1] = coinbase[1].replace('88ac0000000002', '88ac00000000|02')
			coinbase[1] = coinbase[1].replace('88ac0000000003', '88ac00000000|03')
			coinbase[1] = coinbase[1].replace('88ac0000000004', '88ac00000000|04')

			coinbase[1] = coinbase[1].replace('88ac00000000|010000001976a914', '88ac00000000010000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|020000001976a914', '88ac00000000020000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|030000001976a914', '88ac00000000030000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|040000001976a914', '88ac00000000040000001976a914')

			coinbase[1] = coinbase[1].split('|')
		except IndexError:
			pass

		final = []
		final.append(coinbase[0])
		#print("Appended coinbase")

		try:
			for entry in coinbase[1]:
				final.append(entry)
			#print(final)
		except IndexError:
			#print("Single transaction with only coinbase")
			#print(final)
			pass
		return final

		#split = split88ac(tx)
		#return split


	####
	# Pass in an array of the transactions
	#
	def readTx(arr):
		new = []
		inc = 0
		for tx in arr:
			try:
				####
				# Get rid of any stray entries that have nothing in them
				#
				if(tx == ''):
					pass
				else:
					continue
				temp = deserialize(tx)

				new.append(temp)
				#print("Successfully read tx", inc, tx[0:12])
				inc += 1
				
			except (IndexError, binascii.Error) as e:
				print(e)
				print("Error reading tx #" ,inc, "tx = ", tx)
				inc += 1
				pass
		return new

	incr = 0

	split = split88ac(tx)

	btxRead = readTx(split)
	txArr = []

	for tx in btxRead:
		txArr.append([{'btxraw': split[incr], 'btxinfo': tx}])
		incr += 1
	#print(txArr)

	#print(txArr)
#webJson.update({'btx': txArr })