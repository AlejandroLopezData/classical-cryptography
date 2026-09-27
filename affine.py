#Part B2 -- Affine cipher --------------------------------------------------------

from basics import to_numbers, to_letters, egcd, modinv, alphabet

# here we check if a has inverse mod26
def check_a_affine(a):
    g, x, y = egcd(a, 26)

    if g != 1:
        raise ValueError("not valid")

# encript function afine, taking the text to nubers and then apliying the formula.
def encrypt_affine(text: str, a: int, b: int) -> str:
    check_a_affine(a)
    nums = to_numbers(text)
    enc = []

    for n in nums:
        enc.append((a * n + b) % 26)

    return to_letters(enc)

# for decripting we take the mod inv of a and apply the same formula but with it and -b.
def decrypt_affine(text: str, a: int, b: int) -> str:
    ami = modinv(a, 26)
    nums = to_numbers(text)
    dec = []

    for n in nums:
        dec.append((ami * (n - b)) % 26)

    return to_letters(dec)

# we want to return every posible key pair for the afine cipher.
# we check the possible a values and then for each one return all the b values.
def valid_keys_affine() -> list[tuple[int, int]]:
    valid = []

    for a in range(1, 26):
        g, x, y = egcd(a, 26)
        if g == 1:
            valid.append(a)

    keys = []

    for a in valid:
        for b in range(26):
            keys.append((a, b))

    return keys