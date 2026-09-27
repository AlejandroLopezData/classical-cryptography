#Part A — The four basic operations

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#There are 26 letters in the Alphabet. So we can use the index of a string to create a list of the position of the numbers.
def to_numbers(text: str) -> list[int]:
    result = []
    for ch in text.upper():
        if ch in alphabet:
            result.append(alphabet.index(ch))
    return result

# Using the same logic i created the inverse function
# We could add alphabet[n%26] to make sure that the funct doesnt collapse if n >26 if we shift it in other funct
def to_letters(nums: list[int]) -> str:
    letters = ""
    for n in nums:
        letters += alphabet[n%26]
    return letters


# extended euclidean algorithm using recursive algorithm.
def egcd(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return a, 1, 0

    g, x, y = egcd(b, a % b)

    return g, y, x - (a // b) * y

# modular inverse using the egcd
def modinv(a: int, m: int) -> int:
    g, x, y = egcd(a, m)

    if g != 1:
        raise ValueError("the inverse doesent exist")

    return x % m

#Combine the data bytes with the key bytes using XOR operator(^)
def xor_bytes(data, key):
    resultado = bytearray()

    lengthd = len(data)
    lengthk = len(key)

    for i in range(lengthd):
        keyb = key[i % lengthk] # in this case important to add the module bc the key can be repeated.
        datab = data[i]
        resultado.append(datab ^ keyb)

    return bytes(resultado)
