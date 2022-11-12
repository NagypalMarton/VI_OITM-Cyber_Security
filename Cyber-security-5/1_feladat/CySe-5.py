#Feladat: Az EEPROM_DRUMB fájlban megtalálni a AES-128 (128BITes)kulcsot, majd a HEX szöveget visszafejteni ezzel a megtalált kulccsal (AES ECB módszerrel)
# FILE -> Hex-ben van
# from sys import getsizeof  # str bit-jének meghatározásához

# secTextInHex='7a4aa3819f3d5d14fa82dea63648a614a5dd75ee624edb7c849a29a31cea5283'
# key=open('D://Projects//VI_OITM-Cyber_Security-1//Cyber-security-5//1_feladat//eeprom_dump')

# for x in key:
#     x=x.split("|")
#     del x[0]
#     x=bytes.fromhex(str(x[0]).strip())
#     print(f'{x}\t\t- {getsizeof(x)} - {len(x)}')

from Crypto.Cipher import AES
 
key = b'abcdefghijklmnop'
 
cipher = AES.new(key, AES.MODE_ECB)
msg =cipher.encrypt(b'TechTutorialsX!!TechTutorialsX!!')
print (type(msg))
print (msg)

print(msg.encode("hex"))
 
decipher = AES.new(key, AES.MODE_ECB)
print(decipher.decrypt(msg))