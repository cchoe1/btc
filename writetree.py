import json


####
# This file will be used to create the main tree and organize the block data
#
# This file verifies the integrity of the main block chain
def createTree(startpos):
	def returnFileName(num):
		filepath = '/media/calvin/hdd1/firstTree/'
		filenum = str(num)
		fileext = '.json'
		
		file = filepath + filenum + fileext
		return file

	def readJson(num):
		file = returnFileName(num)

		with open(file, "r") as r:
			jsonDict = json.load(r)

		return jsonDict

	def getLastEntry():
		file = '/media/calvin/hdd1/maintree/maintree.txt'
		with open(file, "r") as f:
			for line in f:
				pass
			last = line
			final = line.replace('\n', '')

			# This splits it into an array [0] = line number, [1] = hash for current line
			# Line number is only used for storing into JSON2
			split = final.split('|')

		return split[1]


	def checkMatch(main, check):
		if(main == check):
			return True
		else:
			return False
		
	def loopCheck(newNum):
		x = 0
		while(x < 400000):

			main = getLastEntry()
			#num += 1
			checkJson = readJson(newNum)
			check = checkJson['bprev']
	
			print("Most recently validated hash:    ", main)
			print("Hash to be checked against main: ", check)
	
			stat = checkMatch(main, check)
			
			if(stat == True):
				print("SUCCESS! @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
				print('Line number: ', checkJson['bline'])
				file = '/media/calvin/hdd1/maintree/maintree.txt'

				with open(file, "a") as f:
					f.write(checkJson['bline'])
					f.write('|')
					f.write(checkJson['bcurr'])
					f.write('\n')
				x += 1
	
			else:

				# This number is used to start from a smaller position, instead of 0 everytime
				# Saves computing power
				#
				# There is a chance that you might not find the match, but starting at 99.5% is
				# 	a pretty good start
				newNum = int(newNum * 0.989) + 100

				# If the original search fails, reset to 0, begin searching again
				# This number will set once the first search fails, and then reiterates
				# Until it finds a suitable match


				while(stat != True):
					
					checkJson = readJson(newNum)
					check = checkJson['bprev']

					stat = checkMatch(main, check)
					print("Most recently validated hash:    ", main)
					print("Hash to be checked against main: ", check)

					if(stat == True):
						print("SUCCESS! @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
						print('Line number: ', checkJson['bline'])
						file = '/media/calvin/hdd1/maintree/maintree.txt'
						
						with open(file, "a") as f:
							f.write(checkJson['bline'])
							f.write('|')
							f.write(checkJson['bcurr'])
							f.write('\n')
						x += 1

					else:
						print("No match")
						print('Line number: ', checkJson['bline'])
						newNum += 1
						pass

					
					#while(main['bcurr'] != check['bprev']):
					#	num += 1
		# return main


	loopCheck(startpos)


####
# The call to the main function
#
createTree(200000)