from basics import to_numbers, to_letters, egcd, modinv, alphabet

# B3 — Monoalphabetic substitution --------------------------------------------------------

# we could make a validation function for the key but the code is simple to put it in the function.
def encrypt_mono(text: str, key: str) -> str:
    result = ""

    if len(key) != 26 or len(set(key)) != 26:
        raise ValueError("the key is not valid, check the len and uniq of the letters")

    text_up = text.upper()

    for txt in text_up:
        if txt in alphabet:
            n = alphabet.index(txt)
            result += key[n]

    return result


def decrypt_mono(ciphertext: str, key: str) -> str:
    result = ""

    if len(key) != 26 or len(set(key)) != 26:
        raise ValueError("not a valid key")

    text_up = ciphertext.upper()

    for txt in text_up:
        if txt in key:
            n = key.index(txt)
            result += alphabet[n]

    return result


# we can complete a key from a not valid len key.
def key_from_keyword_affine(keyw: str) -> str:
    key = ""

    for txt in keyw.upper():
        if txt not in key and txt in alphabet:
            key += txt

    for txt in alphabet:
        if txt not in key:
            key += txt

    return key