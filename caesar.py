from basics import to_numbers, to_letters, egcd, modinv, alphabet

#Part B1 -- Caesar cipher --------------------------------------------------------


# in the cesar we shift all the letters with a unique number k.
#to decript we can just apply the same function but with -k.

def encrypt_cesar(plaintext, k):
    numbers = to_numbers(plaintext)
    result = []

    for n in numbers:
        result.append((n + k) % 26)

    return to_letters(result)


def decrypt_cesar(ciphertext, k):
    return encrypt_cesar(ciphertext, -k)