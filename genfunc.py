import binascii

def numToStr(num):
	
	arr = []
	final = []
	if(num <= 9):
		arr.extend(['0','0','0','0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	elif(num > 9 and num <= 99):
		arr.extend(['0','0','0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	elif(num > 99 and num <= 999):
		arr.extend(['0','0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	elif(num > 999 and num <= 9999):
		arr.extend(['0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	else:
		print("Error")
	return final

def toString(arr):
	new = []
	for list in arr:
		string = ''.join(list)
		new.append(string)

	return new

def arrayToString(arr):
	string = ''.join(arr)
	return string

	
def stringToList(string):
	output = string.split()
	return output


# accepts string, turns into byte pairs, 
def toBigEndian(array):

	def listToPairs(listt):
		listed = list(listt)
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
	stringed = arrayToString(single)

	return stringed
