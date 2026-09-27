# B4 — Vigenère --------------------------------------------------------

from basics import to_numbers, to_letters, egcd, modinv, alphabet

# the cipher is the sum of the idx of the txt + the idx of the key mod26.
# the key can have a len btw 1 and the len of the txt.

def encrypt_vigenere(plaintext: str, key: str) -> str:

    if not key or not key.isalpha():
        raise ValueError("the key is not valid")

    result = ""
    key = key.upper()
    plaintext = plaintext.upper()
    lenkey = len(key)
    key_idx = 0

    for char in plaintext:
        if char in alphabet:
            a = alphabet.index(char)
            b = alphabet.index(key[key_idx % lenkey])
            result += alphabet[(a + b) % 26]
            key_idx += 1

    return result


# same as the encrypt but instead of sum we rest in the result form.

def decrypt_vigenere(ciphertext: str, key: str) -> str:

    if not key or not key.isalpha():
        raise ValueError("the key is not valid")

    result = ""
    key = key.upper()
    ciphertext = ciphertext.upper()
    lenkey = len(key)
    key_idx = 0

    for char in ciphertext:
        if char in alphabet:
            a = alphabet.index(char)
            b = alphabet.index(key[key_idx % lenkey])
            result += alphabet[(a - b) % 26]
            key_idx += 1

    return result


# here we want to split the text in groups of letters using the m step.

def cosets(ciphertext: str, m: int) -> list[str]:
    result = []
    leng = len(ciphertext)

    for a in range(m):
        coset = ""

        for i in range(a, leng, m):
            coset += ciphertext[i]

        result.append(coset)

    return result