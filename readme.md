# Cryptography Project

## 1. Introduction

This project implements several classical cryptographic algorithms and basic cryptanalysis techniques.

The implemented ciphers are:

* Caesar cipher

* Affine cipher

* Monoalphabetic substitution cipher

* Vigenère cipher

The project also includes tools for breaking some of these ciphers using frequency analysis and other cryptanalysis techniques.

## 2. How to Run Everything

The program is executed from the command line using:

```
python3 crypto.py <command> <action> [options]

```

### 2.1 Caesar Cipher

Encrypt:

```
python3 crypto.py caesar encrypt --key 3 --in message.txt --out cipher.txt

```

Decrypt:

```
python3 crypto.py caesar decrypt --key 3 --in cipher.txt --out message.txt

```

Breaking:

```
python3 crypto.py break caesar --in cipher.txt --lang en

```

The --lang option specifies the language used for frequency analysis.

### 2.2 Affine Cipher

Encrypt:

```
python3 crypto.py affine encrypt --a 5 --b 8 --in message.txt --out cipher.txt

```

Decrypt:

```
python3 crypto.py affine decrypt --a 5 --b 8 --in cipher.txt --out message.txt

```

The value of a must be coprime with 26.

Breaking:

```
python3 crypto.py break affine --in cipher.txt

```

### 2.3 Monoalphabetic Cipher

Encrypt:

```
python3 crypto.py mono encrypt --keyword CRYPTO --in message.txt --out cipher.txt

```

Decrypt:

```
python3 crypto.py mono decrypt --keyword CRYPTO --in cipher.txt --out message.txt

```

The keyword is used to construct the substitution alphabet.

### 2.4 Vigenère Cipher

Encrypt:

```
python3 crypto.py vigenere encrypt --key LEMON --in message.txt --out cipher.txt

```

Decrypt:

```
python3 crypto.py vigenere decrypt --key LEMON --in cipher.txt --out message.txt

```

Breaking:

```
python3 crypto.py break vigenere --m 5 --in cipher.txt

```

The --m option specifies the assumed length of the Vigenère key.

### 2.6 Input and Output Files

The --in option specifies the input file.

The --out option is optional. If it is provided, the result is written to that file:

```
python3 crypto.py caesar encrypt --key 3 --in message.txt --out cipher.txt

```

If --out is not provided, the result is printed directly to the terminal:

```
python3 crypto.py caesar decrypt --key 3 --in cipher.txt

```

Characters that are not part of the alphabet are ignored during encryption and decryption. Therefore, spaces and punctuation are not preserved in their original positions.

## 3. Key Space Size of the Four Ciphers

### 3.1 Caesar Cipher

The Caesar Cipher uses a single integer shift over the 26 letters of the alphabet.
Therefore the key space is “26”
The shift of 0 is equal to non encryption, thus, there are 25 keys in reality.

### 3.2 Affine Cipher

This cipher uses 2 parameters, (a,b), the value of b can be any of the 26 alphabet positions.
But, a must be relatively prime to 26 so that a modinv exists.
The total number of possible keys is: 12 \* 26 = 312

### 3.3 Monoalphabetic Cipher

The monoalphabetic uses a permutation of the 26 letters. Therefore the keyspace is 26!

### 3.4 Vigenère Cipher

This cipher depends directly on the key length.
For example if we have a key length of 5 we have 26^5 = 11.881.376 different keys in our key space.

## 4. C1 — Measurements

### 4.1 Measurement Setup

To evaluate the reliability and performance of frequency-based cryptanalysis, random text fragments were generated from reference texts in Spanish and English at lengths $L \in \{1, 5, 10, 20, 30, 40, 60, 100\}$. Each fragment was encrypted using a randomly selected key, and the recovery accuracy (percentage of correctly decrypted keys/texts) was measured across three distinct scenarios:

1. **Spanish Text with Spanish Frequency Table**
2. **English Text with English Frequency Table**
3. **English Text evaluated against a Spanish Frequency Table**

---

### 4.2 Data & Results Summary

| Text Length| Spanish | English | English Text + ES Table (Wrong Table) |
|---:|---:|---:|---:|
| **1** | 12.0% | 10.0% | 15.0% |
| **5** | 61.0% | 52.5% | 47.5% |
| **10** | 88.0% | 77.5% | 70.0% |
| **20** | 98.5% | 93.5% | 78.0% |
| **30** | 97.0% | 100.0% | 92.5% |
| **40** | 100.0% | 100.0% | 91.0% |
| **60** | 100.0% | 100.0% | 99.5% |
| **100** | 100.0% | 100.0% | 100.0% |

---

### 4.3 Analysis
The breaker becomes reliable, let's fix a 90% accuracy to measure that. Thus, it becomes reliable reaching the 20 letter length text in both cases EN and ES.
The wrong table costs that in that 20 letter length the cipher is not reliable with a 78%, we need 30 letters to reach the 90%. Thus, we lose a 1/3 of the capacity
to analyze short texts.

## 5. C2 — Comparison with C1

## 6. C3 — Measurements and Analysis

## 7. C4 — Cryptogram and Assistant

## 8. Monoalphabetic Cipher vs AES-128

The monoalphabetic cipher has a key space of:

$$
26! \approx 4 \times 10^{26}
$$

which corresponds to approximately 88 bits of key space. This is larger than the key space of an 88-bit key, but the size of the key space alone does not determine the practical security of a cipher. In a monoalphabetic substitution cipher, each plaintext letter is always replaced by the same ciphertext letter. This preserves statistical properties of the language, such as letter frequencies, repeated patterns, and word structures. These properties can be exploited by a human or by the cryptanalysis assistant to reduce the effective search space dramatically. AES-128 has a key space of ($2^{128}$), but more importantly, it is specifically designed to avoid exploitable statistical relationships of this kind. Therefore, the monoalphabetic cipher can be broken using its structural weaknesses despite its large nominal key space, whereas the same type of frequency-analysis approach does not provide a practical method for recovering an AES-128 key.

## 9. Limitations

Some limitations of the implementation are known.

* Characters outside the project's alphabet are ignored.

* Spaces and punctuation are therefore not preserved in the output.

* Frequency-based cryptanalysis is less reliable when the ciphertext is very short.

* For example, a very short ciphertext such as HELLO is not sufficient to reliably determine the Caesar key using frequency analysis.

* Longer ciphertexts provide more reliable statistical information.

* The cryptanalysis functions may therefore produce incorrect results when insufficient ciphertext is available.

## 10. Conclusion

Final Results

Known Limitations

Possible Improvements