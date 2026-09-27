from frequencies import LETTER_FREQUENCIES
from basics import alphabet
from caesar import decrypt_cesar
from affine import decrypt_affine, valid_keys_affine
from vigenere import cosets, decrypt_vigenere

# C1 — Caesar breaker ---------------------------------------------------------

# with this function we can compare diferent brute force keys and search a low chi sq value to find the key.
#the formula is the normalizedsumatory (observed - expected)^2 / expected) for all letters.

def chi_squared(text: str, table: dict[str, float]) -> float:
    counts = {}

    for let in text.lower():
        if let in table: # we only want to county the letters that we have in our dic.
            counts[let] = counts.get(let, 0) + 1 #(let,0) helps to manage the case when the letter is not in the dic. instad of making none + 1, makes 0+1.

    n = sum(counts.values()) # number of letters in the txt.

    chisq = 0.0

    for let in table:
        obs = counts.get(let, 0)
        exp = table[let] * n

        val = (obs - exp) ** 2 / exp

        chisq += val

    return chisq / n # norm by the number of letters.

# here we brake the cesar iterating 26 times and searching for the best chi2 that should be the correct text...
def break_caesar(ciphertext: str, language: str = "en") -> tuple[int, str]:
    table = LETTER_FREQUENCIES[language]

    bk = 0
    bst_chi = float("inf") # partimos de el maximo valor(infito) para no tener un techo que el chi pueda sobrepasar aunque podriamos poner un numero grande
    bst_txt = ""

    for k in range(26):
        txt = decrypt_cesar(ciphertext, k)
        chiv = chi_squared(txt, table)

        if chiv < bst_chi:
            bk = k
            bst_chi = chiv
            bst_txt = txt

    return bk, bst_txt