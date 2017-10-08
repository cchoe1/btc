import json


####
# This file will be used to create the main tree and organize the block data
#
def createTree(startpos):

	def readJson(num):
		filepath = '/media/calvin/hdd1/firstTree/'
		filenum = str(num)
		fileext = '.json'
		
		file = filepath + filenum + fileext
		with open(file, "r") as r:
			jsonDict = json.load(r)

		return jsonDict

	def checkMatch(num):
		main = readJson(num)
		num += 1
		check = readJson(num)

		if(main[''])
		return main


	checkMatch(startpos)

createTree(0)