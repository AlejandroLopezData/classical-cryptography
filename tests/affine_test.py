import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from affine import check_a_affine, encrypt_affine, decrypt_affine, valid_keys_affine


text = "attack"
a = 5
b = 8

enc = encrypt_affine(text, a, b)
dec = decrypt_affine(enc, a, b)

print("encrypted:", enc)
print("expected:", "IZZISG")
print("eecrypted:", dec)

print("----------------------------")
for a in [0, 2, 13, 26]:
    try:
        check_a_affine(a)
        print("a =", a, "accepted")
    except ValueError:
        print("a =", a, "raises ValueError")

print("----------------------------")

keys = valid_keys_affine()
print("number of the valid keys of affine:", len(keys))