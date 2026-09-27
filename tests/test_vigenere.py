import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from vigenere import encrypt_vigenere, decrypt_vigenere, cosets


# testing encripting and decripting
print("encrypt(MYSECRETMESSAGE):", encrypt_vigenere("MYSECRETMESSAGE", "KEY"))
print("decrypt:",decrypt_vigenere("WCQOGPOXKOWQKKC", "KEY"))

print("encrypt(attackatdawn):", encrypt_vigenere("attackatdawn", "LEMON"))
print("decrypt:",decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))

#testing cosets
print("cosets(ABCDEF, 3):",cosets("ABCDEF", 3))

#testing error cases
try:
    encrypt_vigenere("HELLO", "")
except ValueError:
    print("ev an empty key: ValueError")


try:
    encrypt_vigenere("HELLO", "KEY123")
except ValueError:
    print("ev a non alphabetic key: ValueError")