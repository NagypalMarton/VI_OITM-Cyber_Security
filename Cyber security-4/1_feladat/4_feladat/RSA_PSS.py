#Adott mondat: Continental - The Future in Motion
#Hash -> SHA256
#RSA key hossz: 2048bit
#kulcspár: .pem
#RSA PSS aláírás
#Add meg azt a RSA PSS aláírást, amelyik a fenti jelmondatra lett generálva!

# from Crypto.PublicKey import RSA
# from Crypto.Random import get_random_bytes
# from Crypto.Cipher import AES, PKCS1_OAEP

# data = "Continental - The Future in Motion".encode("utf-8")
# file_out = open("encrypted_data.bin", "wb")

# recipient_key = RSA.import_key(open("D:\Projects\VI_OITM-Cyber_Security\Cyber security-4\\1_feladat\\4_feladat\public_key.pem").read())
# session_key = get_random_bytes(16)

# # A munkamenetkulcs titkosítása a nyilvános RSA-kulccsal
# cipher_rsa = PKCS1_OAEP.new(recipient_key)
# enc_session_key = cipher_rsa.encrypt(session_key)

# # Az adatok titkosítása az AES munkamenetkulccsal
# cipher_aes = AES.new(session_key, AES.MODE_EAX)
# ciphertext, tag = cipher_aes.encrypt_and_digest(data)
# [ file_out.write(x) for x in (enc_session_key, cipher_aes.nonce, tag, ciphertext) ]
# file_out.close()
# print(enc_session_key)
from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random

message = 'Continental - The Future in Motion'
try:
    key = RSA.import_key(open('D:\Projects\VI_OITM-Cyber_Security\Cyber security-4\\1_feladat\\4_feladat\private_key.pem').read())
    h = SHA256.new(message)
    signature = pss.new(key).sign(h)
    print(signature)
except (ValueError, TypeError):
    print(f"Hiba!\n{ValueError.args} - {TypeError}")
for x in range(4):
    print(x)