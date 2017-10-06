from genfunc import *

def openFile(fnum, lin):
	#takes input number, converts it to proper formatted string with leading 0s
	numstr = numToStr(fnum)
	
	#takes a number generated above to choose the proper file
	def chooseFile(numstr):
		fs = '/media/calvin/hdd1/step1/blk'
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

	

	print("Your filenumber is: ", numstr)
	print("Your block number is: ", contents[0])

	print("\n")


	# returns a list containing 2 elements: 0 - block #, 1 - block contents
	return contents


#openFile( {file number}, {line number} ), 0 index starting point
# fileContent = openFile(0,1)

# print(fileContent)

#next create controller to loop through every line of every file and parse it
