from Crypto.Cipher import AES
import random
import string
import binascii


mydict={}

#Here I try all keys and I add the encryption in the table
for j in xrange(16777215):
	tempA = str(bin(j)[2:].zfill(24))

	table =[hex(int(tempA[0:8],2))[2:].zfill(2),hex(int(tempA[8:16],2))[2:].zfill(2), hex(int(tempA[16:24],2))[2:].zfill(2),"00","00","00","00","00","00","00","00","00","00","00","00","00"]
	#print table
	temp = ""
	#print table
	for i in xrange(len(table)):
		temp = temp + chr(int(table[i], 16))


	key = temp
	#print key
	cipher = AES.new(key, AES.MODE_ECB)
	#test = bin(int("00aef493ab258aaa0dfe6ef8fdee11fd", 16))[2:].zfill(128)
	msg = cipher.encrypt( "00aef493ab258aaa0dfe6ef8fdee11fd".decode("hex")).encode("hex")
	mydict[msg] = table

"""for item in mydict:
	print item
	print mydict[item]
"""
print "Step 2"

#Then I try all keys for decrypt and I check in the dictionnary
for x in xrange(16777215):
	tempA = str(bin(x)[2:].zfill(24)) 	

	table =[hex(int(tempA[0:8],2))[2:].zfill(2),hex(int(tempA[8:16],2))[2:].zfill(2), hex(int(tempA[16:24],2))[2:].zfill(2),"00","00","00","00","00","00","00","00","00","00","00","00","00"]
	#print table
	temp = ""
	for i in xrange(len(table)):
		temp = temp + chr(int(table[i], 16))
	key = temp
	decipher = AES.new(key, AES.MODE_ECB)
	val = decipher.decrypt("b252c4647ee03532c56c95c43b378070".decode("hex")).encode("hex")
	if  val in mydict:
		print "key 1", mydict[val]
		print "key 2", table
		break