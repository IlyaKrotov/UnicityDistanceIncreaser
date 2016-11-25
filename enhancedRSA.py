import rsa
import UnicityDistanceIncreaser

def encrypt(message, public_key):
	message = UnicityDistanceIncreaser.EncryptText(message)
	strs = []; i = 0; crypto = []
	
	while i < (len(message)):
		strs.append(str(message[i:i+52]))
		i = i + 52

	for i in range(len(strs)):
		crypto.append(rsa.encrypt(strs[i], public_key))

	return crypto

def decrypt(crypto, private_key):
	recvMessage = []; decrRecvMessage = ""
	for i in range(len(crypto)):
		recvMessage.append(rsa.decrypt(crypto[i], private_key))
		decrRecvMessage += recvMessage[i]

	result = UnicityDistanceIncreaser.DecryptText(decrRecvMessage)

	return result

def newkeys(n):
	return rsa.newkeys(n)