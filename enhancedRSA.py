import rsa
import UnicityDistanceIncreaser

def encrypt(message, public_key):
	message, isCompressed = UnicityDistanceIncreaser.EncryptText(message)
	strs = []; i = 0; crypto = []
	
	while i < (len(message)):
		strs.append(str(message[i:i+52]))
		i = i + 52

	for i in range(len(strs)):
		crypto.append(rsa.encrypt(strs[i], public_key))

	return crypto, isCompressed

def decrypt(crypto, private_key):
	recvMessage = []; decrRecvMessage = ""
	for i in range(len(crypto)):
		recvMessage.append(rsa.decrypt(crypto[i], private_key))
		decrRecvMessage += recvMessage[i]

	result = UnicityDistanceIncreaser.DecryptText(decrRecvMessage)

	return result


def codeParamsEncrypt(paramsFile="coder_parameters.txt", public_key)):
	params = rsa.encrypt(UnicityDistanceIncreaser.CodeParameters(paramsFile), public_key)
	return params


def codeParamsDecrypt(encryptedParameters, private_key, parametersFile="coder_parameters.txt"):
	paramsString = rsa.decrypt(encryptedParameters, private_key)
	params = paramsString.split(" ")

	paramsFile = open(parametersFile, "w")
    paramsFile.write(paramsString)
    paramsFile.close()

	return params

def newkeys(n):
	return rsa.newkeys(n)