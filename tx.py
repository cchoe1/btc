import binascii

x = '../blocks/blk00000.dat'

def readFile(x):
	with open(x, 'rb') as f:
		hexdata = binascii.hexlify(f.read())

		print("File Read")
		return hexdata

def combineHex(hex):
	arr = list(hex)
	#arr.remove('\'')
	#arr.pop(0)

	print("combineHex() complete")
	return arr

# accepts list of digits, forms byte pairs, returns array of arrays
def groupHex(arr):
	final = []
	key = 0
	leng = len(arr)
	leng -= 1

	while (key < leng):
		array = []
		inc = 0
		while (inc < 2):
			array.append(arr[key])
			key += 1
			inc += 1
		final.append(array)
		print(key)
	return final[0:5]

read = readFile(x)

combine = combineHex(read)

group = groupHex(combine)