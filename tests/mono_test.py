import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from monoalpha import encrypt_mono, decrypt_mono, key_from_keyword_affine


key = key_from_keyword_affine("CRYPTO")
print("key_from_keyword:", key)

key = "MNBVCXZASDFGHJKLPOIUYTREWQ"

print("encrypthello:", encrypt_mono("HELLO", key),":correct")
print("encryptbob:", encrypt_mono("BOB", key),":correct")