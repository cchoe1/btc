from readfile import *
from readblock import *
from writejson import *
#from analyzeblock import *

####
# This file will write the first json files - the raw hex

####
# We pass the file number + the line of each file into this controller, which loops through everything 
# 	or can find specific information
#
filenum = 80
blocknum = 0


####
# Begin loop - choose starting file & starting block num (suggested: 0 start)
# Automatically stops after the next file cannot be found
#


while(blocknum < 5):

	####
	# Specify how many files you want it to iterate
	#
	if(filenum > 305):
		break

	else:
	
		try:
			print("---------------------")
			
			####
			# 0 index = # of lines, line # starts at 1
			# openFile( {file number} , {line number} )
			#
			var = openFile(filenum,blocknum)
	
	
			####
			# This function takes in an array with 2 arrays inside - [0] is the block line number, [1] is the raw block hex
			#
			#
			compiled = compileBlock(var)
	
	
			####
			# This will create a Python dictionary for various analytics that will be shown
			# 	on the website, such as UTC time, prev, next, current hash, etc.
			#
			#web = analysisForWeb(compiled)
			writeFirstJson(compiled)
			print("File number = ", filenum)
			print("Block num = ", blocknum)
			blocknum += 1
	
		####
		# This runs after we reach the end of a file and hit an IndexError
		# Then it resets the blocknum to 0 and increments to the next file
		#
		# Note:  You cannot write to an erroneous file -- at worst, you might skip one
		# 	But the file number is retained within the JSON object so it cannot be 
		# 	written to an erroneous name - when other programs run, this chain will
		# 	be double-validated since the program will stop if it can't find a file
		#
		# 	aka - if you miss a file, you don't have to rewrite them all, just find
		# 	the missing file and write it in
		except IndexError:
			print("End of file")
			blocknum = 0
			filenum += 1