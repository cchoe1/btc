def numToStr(num):
	
	arr = []
	final = []
	if(num <= 9):
		arr.extend(['0','0','0','0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	elif(num > 9 and num <= 99):
		arr.extend(['0','0','0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	elif(num > 99 and num <= 999):
		arr.extend(['0','0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	elif(num > 999 and num <= 9999):
		arr.extend(['0'])
		arr.extend(list(str(num)))
		final = ''.join(arr)
	else:
		print("Error")
	return final