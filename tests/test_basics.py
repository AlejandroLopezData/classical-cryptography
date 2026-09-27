import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from basics import to_letters, to_numbers, egcd, modinv, xor_bytes


print("modinv(5, 26) =", modinv(5, 26))
print("modinv(7, 26) =", modinv(7, 26))
print("modinv(17, 26) =", modinv(17, 26))

try:
    modinv(13, 26)
except ValueError:
    print("modinv(13, 26) raises ValueError")

try:
    modinv(2, 26)
except ValueError:
    print("modinv(2, 26) raises ValueError")

print('xor_bytes(b"HELLO", b"KEYKE").hex() =',xor_bytes(b"HELLO", b"KEYKE").hex())

print("to_letters(to_numbers(HELLO)) =",to_letters(to_numbers("HELLO")))

print("emptycase:", to_numbers(""))
print("single case:", to_letters(to_numbers("A")))