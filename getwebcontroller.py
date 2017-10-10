from getwebjson import *
from writejson import *
from readfile import *

#webjson = analysisForWeb(1)

#print("The json = ", webjson['_id'])

x = 11500
while(x < 11510):
	####
	#
	#
	#
	line = readTree(x)


	####
	#
	#
	#
	webjson = analysisForWebB(line[0])
	webjson.update({'_id': str(x)})

	print(webjson)

	
	####
	#
	#
	#
	#writeThirdJson(webjson, x)

	x += 1




