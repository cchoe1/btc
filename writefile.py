import binascii
from genfunc import *


#used internally to generate filenames
def writeFile(filenum):

	def returnFileName(type, number, ext):
		num = str(number)
	
		final = type + num + ext
	
		return final
	
	def readData(fin):
		x = returnFileName('/media/calvin/hdd1/blocks/blk', fin, '.dat')
		with open(x, 'rb') as f:
			hexdata = binascii.hexlify(f.read())
			output = str(hexdata)
			hexdata = ''
	
			print("File Read")
		return output
	
	def combineHex(hex):
		arr = list(hex)
		arr.pop(0)
		arr.pop(0)
	
		print("combineHex() complete")
		return arr
	
	def toString(hex):
		hold = ''.join(hex)
		return hold
	
	# accepts a string and removes MagicID  -creates blocks
	def splitParse(string):
		char = 'f9beb4d9'
		data = string.split(char)
		data.pop(0)

		return data
	
	def write(data, filenum):
		fin = numToStr(filenum)
		file = returnFileName('/media/calvin/hdd1/step1/blok', fin, '.txt')

		#returns starting number point
		def readLastLine(filenum, data):
			lastFileNum = filenum - 1
			num = numToStr(lastFileNum)
			fileName = returnFileName('/media/calvin/hdd1/step1/blok', num, '.txt')

			with open(fileName, 'r') as prevFile:
				for line in prevFile:
					firstLine = line
					pass
				lastLine = line
				print('Prev Last line = ', lastLine)
			inte = int(firstLine) + 1

			print('New start line', inte)

			
			return(inte)
		
		def addData(data, file, start):
			inc = 0
			length = len(data) - 1
			lastIndex = length + start

			with open(file, "w") as w:
				length = len(data)
				strleng = len(str(length))

					
				w.write(str(start) + '\n')
				while (inc < length):
					w.write(data[inc])
					w.write('\n')
					inc += 1
				w.write(str(lastIndex))

				print('New last line = ', lastIndex)
				print("Done writing to file: " , file)

		if(filenum == 0):
			addData(data, file, 0)
		else:

			firstNum = readLastLine(filenum, data)
			addData(data, file, firstNum)
 


	##################################################################
	########################### MAIN #################################
	##################################################################
	
	# create logic controller to loop through each num, first converting to int
	# so that it can be incremented and looped through until the last file designated
	# probably want to design it so that you just select which files you want to upload
	# otherwise we would probably spend a lot of computing power on redoing files
	
	#create loop that loops through everything below but increments filename by 1 each time
	
	####
	# sets filenumber
	# returns integer as string with leading zeros
	#
	numString = numToStr(filenum)
	
	####
	# readData( {filenumber} )
	#
	#
	#
	file = readData(numString)
	
	####
	# combineHex( {filename} )
	#
	#
	#
	combined = combineHex(file)
	
	####
	# toString( {array of chars} )
	#
	#
	#
	string = toString(combined)
	
	####
	# splitParse( {single string} , {string to search} )
	#
	#
	split = splitParse(string)

	# completed = addNumber(split)
	
	####
	# writeFile( {list of blocks} , {filenumber} )
	#
	#
	#
	write(split, filenum)




