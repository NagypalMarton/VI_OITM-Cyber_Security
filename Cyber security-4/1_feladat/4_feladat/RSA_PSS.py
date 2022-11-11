# Adott mondat: Continental - The Future in Motion
# Hash -> SHA256
# RSA key hossz: 2048bit
# kulcspár: .pem
# RSA PSS aláírás
# Add meg azt a RSA PSS aláírást, amelyik a fenti jelmondatra lett generálva!

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

message = b'Continental - The Future in Motion'
public_key = RSA.import_key(open('D://Projects//VI_OITM-Cyber_Security-1//Cyber security-4//1_feladat//4_feladat//public_key.pem').read())

option_sign=open('D://Projects//VI_OITM-Cyber_Security-1//Cyber security-4//1_feladat//4_feladat//option_1_sign.txt')
signature=bytes.fromhex(option_sign.read())

h = SHA256.new(message)
verifier=pss.new(public_key)
try:
    verifier.verify(h,signature)
    print("Az aláírás jó!")
except(ValueError,TypeError):
    print('Az aláírás nem jó!')