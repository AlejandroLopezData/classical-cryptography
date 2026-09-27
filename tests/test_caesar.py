import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from caesar import encrypt_cesar, decrypt_cesar


text = "MYSECRETMESSAGE"
k = 3

enc = encrypt_cesar(text, k)
dec = decrypt_cesar(enc, k)

print("encrypted:", enc)
print("expected:", "PBVHFUHWPHVVDJH")
print("decrypted:", dec)

print("------------------------------")

# test the k values with values outside
for k in [0, 1, 25, 26, 27, -1, 52]:
    enc = encrypt_cesar(text, k)
    dec = decrypt_cesar(enc, k)

    print("k =", k, "correct:", dec == text)