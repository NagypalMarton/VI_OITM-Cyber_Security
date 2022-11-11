from Crypto.Cipher import AES
key=bytes.fromhex('7a4aa3819f3d5d14fa82dea63648a614a5dd75ee624edb7c849a29a31cea5283')
#Kódolás
cipher=AES.new(key,AES.MODE_ECB)
print(key)
# msg=cipher.encrypt(bytes.fromhex(open('D://Projects//VI_OITM-Cyber_Security-1//Cyber-security-5//1_feladat//eeprom_dump').read()))
# print(type(msg))
# print(msg.encode("hex"))

# #Dekódols
# decipher = AES.new(key, AES.MODE_ECB)
# print(decipher.decrypt(msg))