from genfunc import *

def openFile(fnum, lin):
	#takes input number, converts it to proper formatted string with leading 0s
	numstr = numToStr(fnum)
	
	#takes a number generated above to choose the proper file
	def chooseFile(numstr):
		fs = '/media/calvin/hdd/step1/blok'
		fext = '.txt'
		fileName = fs + numstr + fext
		return fileName

	file = chooseFile(numstr)

	def readFile(filename, lin):

		with open(filename, "r") as r:#, open('blok1test.txt', "w") as w:
			arr = []
			final = []

			for line in r:
				arr.append(line)
			    #print(str(line))
			#arr.pop(1)
			arr[lin].replace('\'\n', '')
			startPoint = int(arr[0])
			print("The starting point = ", startPoint)
			blockNo = lin + startPoint

			final.append([blockNo])
			arr.pop(0)
			arr.pop(len(arr) - 1)
			final.append([arr[lin]])
		return final

	contents = readFile(file, lin)

	# print("Error!")
	# 	return False

	

	print("Your filenumber is: ", numstr)
	print("Your block number is: ", contents[0])

	print("\n")


	# returns a list containing 2 elements: 0 - block #, 1 - block contents
	return contents



####
# This function is responsible for returning a plain raw line
#
#

def returnRaw(fnum, lin):
	temp = 0


####
# This function is responsible for reading the maintree.txt and writing the json files to the correct name order
#
#
def readTree(num):
	file = '/media/calvin/hdd/maintree/maintree.txt'
	with open(file, 'r') as f:
		for i, line in enumerate(f):
			if(i == num):
				hold = line
				break
	split = hold.split('|')
	
	final = []
	final.append(split[0])
	final.append(split[1].replace("\n", ''))

	return final