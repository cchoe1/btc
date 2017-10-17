from bitcoin import *

def splitTx(tx):

	def getCoinbase(array):
		new = []
		####
		# Gets the first transaction by splitting by the checksum + locktime
		#
		new = array.replace('ac0000000001', 'ac00000000|01', 1)
		final = new.split('|')
		#print(final)
		if(len(final) > 0):
			#print("Matched with 01")
			return final
		new = array.replace('ac0000000002', 'ac00000000|02', 1)
		final = new.split('|')
		if(len(final) > 0):
			#print("Matched with 02")
			return final
		new = array.replace('ac0000000003', 'ac00000000|03', 1)
		final = new.split('|')
		if(len(final) > 0):
			#print("Matched with 03")
			return final
		new = array.replace('ac0000000004', 'ac00000000|04', 1)
		final = new.split('|')
		if(len(final) > 0):
			#print("Matched with 04")
			return final
		
		new = array.split('ac00000000', 1)
		print("ONLY COINBASE IN THIS TX!!")
		####
		# This will remove a stray entry on the end if the block only contains 1 transaction
		#
		if(new[1] == ''):
			removed = new.pop()
			print("Only 1 tx!")
		return new


		# if(array.replace('ac0000000001', 'ac00000000|01') == True):
		# 	new = array.replace('ac0000000001', 'ac00000000|01', 1)
		# 	final = new.split('|')
		# 	return final
		# 	print("Coinbase broken up at 01")
		# elif(array.replace('ac0000000002', 'ac00000000|02') == True):
		# 	new = array.replace('ac0000000002', 'ac00000000|02', 1)
		# 	final = new.split('|')
		# 	return final
		# 	print("Coinbase broken up at 02")
		# elif(array.replace('ac0000000003', 'ac00000000|03') == True):
		# 	new = array.replace('ac0000000003', 'ac00000000|03', 1)
		# 	final = new.split('|')
		# 	return final
		# 	print("Coinbase broken up at 03")
		# elif(array.replace('ac0000000004', 'ac00000000|04') == True):
		# 	new = array.replace('ac0000000004', 'ac00000000|04', 1)
		# 	final = new.split('|')
		# 	return final
		# 	print("Coinbase broken up at 04")
		# else:
		# 	new = array.split('ac00000000', 1)
		# 	print("ONLY COINBASE IN THIS TX!!")
		# 	####
		# 	# This will remove a stray entry on the end if the block only contains 1 transaction
		# 	#
		# 	if(new[1] == ''):
		# 		removed = new.pop()
		# 		print("Only 1 tx!")
		# 	return new

		

		

	def split88ac(string):
		coinbase = getCoinbase(string)

		try:
			coinbase[1] = coinbase[1].replace('88ac00000000010000', '88ac00000000|010000')
			coinbase[1] = coinbase[1].replace('88ac00000000020000', '88ac00000000|020000')
			coinbase[1] = coinbase[1].replace('88ac00000000030000', '88ac00000000|030000')
			coinbase[1] = coinbase[1].replace('88ac00000000040000', '88ac00000000|040000')

			coinbase[1] = coinbase[1].replace('88ac00000000|010000001976a914', '88ac00000000010000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|020000001976a914', '88ac00000000020000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|030000001976a914', '88ac00000000030000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|040000001976a914', '88ac00000000040000001976a914')

			coinbase[1] = coinbase[1].replace('88ac00000000|01976a914', '88ac0000000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|01976a914', '88ac0000000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|01976a914', '88ac0000000001976a914')
			coinbase[1] = coinbase[1].replace('88ac00000000|01976a914', '88ac0000000001976a914')

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


	####
	# Pass in an array of the transactions
	#
	def readTx(arr):
		new = []
		inc = 0
		hold = ''
		for tx in arr:
			tx = hold + tx
			tx = tx.replace('\'', '')
			try:
				#hold = ''
				####
				# Get rid of any stray entries that have nothing in them
				#
				if(tx == ''):
					print('Skipped invalid!', tx)
					continue
				temp = deserialize(tx)

				new.append(temp)
				#print("Successfully read tx", inc, tx)
				inc += 1
				
			except (IndexError, binascii.Error) as e:
				print(e)
				print("Error reading tx #" ,inc, "tx = ", tx)
				#hold = tx
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
	return txArr
#webJson.update({'btx': txArr })