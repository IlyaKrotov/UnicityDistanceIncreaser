import unireedsolomon.rs as rs
import zlib
import math
import random

def fact(j):
    f=1; k=0
    while k<j:
        k=k+1
        f=f*k
    return f

def bn(n, t):
    k=0; c=0
    while k<t or k==t:
        c+=fact(n)/(fact(k)*fact(n-k))
        k+=1
    return c

def Encrypt(textFile, parametersFile="coder_parameters.txt", encryptedFile="encrypted.txt"):
    file = open(textFile, "rb")
    textForTransform = file.read(255)
    file.close()

    l1 = float(len(textForTransform))
    #compress
    compressedText = zlib.compress(textForTransform)
    l2 = float(len(compressedText))
    alpha = l2/l1

    t = 0
    for i in range(int(l2)):
        if alpha - (1-math.log(float(bn(l2, i+1)))/float(l2)) > 0 and alpha - (1-math.log(float(bn(l2, i)))/float(l2)) < 0:
            t = i
            break

    #encode
    coder = rs.RSCoder(min(255, int(l2)+2*t+1), int(l2))
    codedText = coder.encode(compressedText)
    l3 = len(codedText)

    #save params of coder
    paramsFile = open(parametersFile, "w")
    paramsFile.write(str(min(255, int(l2)+2*t+1)) + "\n" + str(int(l2)))
    paramsFile.close()

    #generate and add errors
    errorPlaces = []
    textWithError = codedText
    for i in range(t):
        errorPlaces.append(random.randint(1, l3-1))
        textWithError = textWithError[:errorPlaces[i]-1] + "\0" + textWithError[errorPlaces[i]:]

    #save results 
    encResult = open(encryptedFile, "wb")
    encResult.write(textWithError)
    encResult.close()

    #some results
    print("Text has increased in " + str(float(l3)/l1) + " times")
    print("Compress coef (alpha) = " + str(alpha))
    print("Reed Solomone code parameters: t = " + str(t) + ", N = " + str(min(255, int(l2)+2*t+1)) + ", K = " + str(int(l2)))

    if alpha > 1.0:
        return textForTransform
    else:
        return textWithError

def Decrypt(encryptedFile="encrypted.txt", paramsFile="coder_parameters.txt"):
    encrFile = open(encryptedFile, "rb")
    textForDecrypt = encrFile.read(255)
    encrFile.close()

    paramsFile = open(paramsFile, "rb")
    parameters = [int(line) for line in paramsFile]

    coder = rs.RSCoder(parameters[0], parameters[1])

    decodedText = coder.decode(textForDecrypt)
    decompressedText = zlib.decompress(decodedText[0])

def EncryptText(textForTransform, parametersFile="coder_parameters.txt", encryptedFile="encrypted.txt"):
    print(textForTransform)
    l1 = float(len(textForTransform))
    #compress
    compressedText = zlib.compress(textForTransform)
    l2 = float(len(compressedText))
    alpha = l2/l1

    t = 0
    for i in range(int(l2)):
        if alpha - (1-math.log(float(bn(l2, i+1)))/float(l2)) > 0 and alpha - (1-math.log(float(bn(l2, i)))/float(l2)) < 0:
            t = i
            break

    #encode
    coder = rs.RSCoder(min(255, int(l2)+2*t+1), int(l2))
    codedText = coder.encode(compressedText)
    l3 = len(codedText)

    #save params of coder
    paramsFile = open(parametersFile, "w")
    paramsFile.write(str(min(255, int(l2)+2*t+1)) + "\n" + str(int(l2)))
    paramsFile.close()

    #generate and add errors
    errorPlaces = []
    textWithError = codedText
    for i in range(t):
        errorPlaces.append(random.randint(1, l3-1))
        textWithError = textWithError[:errorPlaces[i]-1] + "\0" + textWithError[errorPlaces[i]:]

    #save results 
    encResult = open(encryptedFile, "wb")
    encResult.write(textWithError)
    encResult.close()

    #some results
    print("Text has increased in " + str(float(l3)/l1) + " times")
    print("Compress coef (alpha) = " + str(alpha))
    print("Reed-Solomone code parameters: t = " + str(t) + ", N = " + str(min(255, int(l2)+2*t+1)) + ", K = " + str(int(l2)))

    if alpha > 1.0:
        return textForTransform
    else:
        return textWithError

def DecryptText(textForDecrypt, paramsFile="coder_parameters.txt"):
    paramsFile = open(paramsFile, "rb")
    parameters = [int(line) for line in paramsFile]

    coder = rs.RSCoder(parameters[0], parameters[1])

    decodedText = coder.decode(textForDecrypt)
    decompressedText = zlib.decompress(decodedText[0])

    return decompressedText

