from readfile import *
from readblock import *
from writejson import *
from analyzeblock import *


###########################################
# The idea is that we run 2 main programs:
# One writes files, one reads files
#
###########################################


# We pass the file number + the line of each file into this controller, which loops through everything 
# 	or can find specific information
#
filenum = 0
blocknum = 100000
while(blocknum < 110000):
	print("---------------------")
	
	# 0 index = # of lines, line # starts at 1
	# openFile( {file number} , {line number} )
	#
	var = openFile(filenum,blocknum)
	
	
	# This function takes in an array with 2 arrays inside - [0] is the block line number, [1] is the raw block hex
	#
	#
	compiled = compileBlock(var)
	
	
	# This will create a Python dictionary for various analytics that will be shown
	# 	on the website, such as UTC time, prev, next, current hash, etc.
	#
	web = analysisForWeb(compiled)
	
	
	blocknum += 1
	#storeJson(compiled)


# print("Compiled = ", compiled['bhash'])


# while (inc < 3):
# 	var = openFile(0,inc)
# 	compiled = compileBlock(var)

# 	inc += 1


	


#############################################

############# User Interface ################

#############################################

# print("Hello Calvin, Welcome Back")


# input(choice)
# while (choice <= 0):
# 	print("Please input a command")
# 	if(choice == '1'):
# 		var = openFile(0,1)
	
# 		compiled = compileBlock(var)
	
# 		print(compiled[577])
	
# 	elif(choice == '2'):
# 		print("You picked 1")
# 		length = int(openFile(0,0))
# 		print(length)

# 		choice = 0
	
# 	elif(choice == '9'):
# 		print("You picked 9.  Hit 9 again to exit")
# 		choice = 0
	
# 		input(choice)
	
# 		if(choice == '9'):
# 			choice = 0
# 			break

# 		else:
# 			print("I'm sorry.  I didn't recognize that command.  Exiting to main menu")
# 			choice = 0
# 			input(choice)

# 	else:
# 		print("I'm sorry.  I didn't recognize that command")
# 		choice = 0
