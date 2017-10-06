# import transaction
# import json

# test = transaction.deserialize('010000000199c867eb7fe692d3e9e700f42e401fcc957a794188d4590f284a948cc9d44b910100000000ffffffff01e8030000000000001976a914ea18a38e2119616d05fbb31a2138f43565608d7c88ac00000000')

# #print(test["outs"])

# string = str(test)
# string.replace('\"', "\'")


# print(test['ins'][0]['sequence'])

# # good = json.dumps(string)
# # python_obj = json.loads(good)

# # print(python_obj['version'])

# arr = ['4','3','2','1']

# arr2 = [['4','3'],['2','1']]

# string = ''.join(arr)

# string2 = ''.join(arr2[0])
# string3 = ''.join(arr2[1])

# comb = string2 + string3

# print(string)
# print(string2)

# print(comb)


def hi():
	print("Hello")


def control():
	hi()

control()