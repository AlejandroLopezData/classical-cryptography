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

## 4. C1 — Break Caesar performance

### 4.1 Measurement Setup

To evaluate the reliability and performance of the Break Caesar frequency based cryptanalysis, two random stories in Spanish and English were generated from which the different length texts came. Each fragment was encrypted using a randomly selected key, and the recovery accuracy (percentage of correctly decrypted keys/texts) was measured across three diferent scenarios:

1. **Spanish Text and Spanish Frequency Table**
2. **English Text and English Frequency Table**
3. **Spanish Text and English Frequency Table "using the wrong table"**

---

### 4.2 Data & Results Summary

| Text Length| Spanish | English | ES Text + ENG Table |
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

## 5. C2 — Break Affine performance

### 4.1 Measurement Setup

Same as Caesar's but dealing with a higher key space.

### 4.2 Data & Results Summary
| Length | ES | EN | ES Text + ENG Table |
|---:|---:|---:|---:|
| 1 | 0.5% | 0.5% | 1.0% |
| 5 | 14.0% | 10.5% | 11.5% |
| 7 | 28.5% | 26.0% | 18.0% |
| 10 | 51.5% | 31.5% | 32.5% |
| 20 | 85.5% | 74.0% | 53.5% |
| 30 | 97.5% | 87.5% | 66.0% |
| 40 | 97.5% | 97.5% | 75.0% |
| 60 | 97.0% | 100.0% | 82.5% |
| 100 | 100.0% | 100.0% | 97.5% |


### 4.3 C3 — Measurements and Analysis

#### Number of candidates tested:
For the affine cipher, the breaker tries every combination of a and b. a must be coprime with 26, thus, there are only 12 valid values for a.
This gives us 12 x 26 = 312 candidate keys

#### Shortest reliable length and comparison with C1:
Using the same 90% reliability threshold defined earlier, the affine at length 30 for ES texts and 40 for ENG texts.
Using the wrong frequency table we can't reach the 90% of reliability until the length of 100.

Comparison with the Caesar's - C1
The Caesar's breaker reached the 90% with length 20 in both lengths, the affine needs higher texts x1.5 and x2 compared with the caesar's.


## 7. Monoalphabetic Cipher vs AES-128

The key space size is not the important thing here, what matters is if the cipher leaks information or not. The monoalphabetic cipher always maps the same plaintext letter to the same ciphertext letter, so things like letter frequency, common patterns and word shapes stay visible even after encrypting. Thats why the C4 assistant (or a human) doesnt need to try the 26! keys, it just guesses the most frequent letters and from there the rest falls into place pretty fast. AES-128 is different, even with a smaller key space of 2^128, it doesnt leak any of this info because of confusion and diffusion, so there is no shortcut and the only way to break it is trying the full key space, which is not feasible in practice.

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