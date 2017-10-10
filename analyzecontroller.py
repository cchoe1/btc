from writejson import *
from analyzeblock import *
from genfunc import *

# This sets the starting point by grabbing the data associated with block x
# analysisForWeb() will open the first json files - the unordered raw hex (little endian)
# 
# Then we get the header, block hash, timestamp, etc. from this
#
# analysisForWeb is used for generating JSON file that will supply the web page with info
# Also can pass the values into writeFirstJson

x = 192000

while(x < 300000):
	json = analysisForWeb(x)
	
	
	
	writeSecJson(json)

	x += 1