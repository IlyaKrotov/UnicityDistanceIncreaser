import enhancedRSA

file = open("test.txt", "rb")
message = file.read(255)
file.close()

(bob_pub, bob_priv) = enhancedRSA.newkeys(512)
crypto = enhancedRSA.encrypt(message, bob_pub)

result = enhancedRSA.decrypt(crypto, bob_priv)

print(result)