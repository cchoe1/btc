from getwebjson import *
from writejson import *

#webjson = analysisForWeb(1)

#print("The json = ", webjson['_id'])

x = 0
while(x < 100000):
	####
	#
	#
	#
	#line = readTree(x)



	####
	#
	#
	#
	webjson = analysisForWebB(x)
	webjson.update({'_id': str(x)})


	
	####
	#
	#
	#
	writeThirdJson(webjson, x)

	x += 1




