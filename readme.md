# Cryptography Project

*Classical ciphers, cryptanalysis, and frequency-analysis attacks implemented in Python.*

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [How to Run Everything](#2-how-to-run-everything)
3. [Key Space Size of the Four Ciphers](#3-key-space-size-of-the-four-ciphers)
4. [C1 — Break Caesar Performance](#4-c1--break-caesar-performance)
5. [C2 — Break Affine Performance](#5-c2--break-affine-performance)
6. [C3 — Break Vigenère Performance](#6-c3--break-vigenère-performance)
7. [Monoalphabetic Cipher vs AES-128](#7-monoalphabetic-cipher-vs-aes-128)
8. [Limitations and Improvements](#8-limitations-and-improvements)

---

## 1. Introduction

This project implements several classical cryptographic algorithms and basic cryptanalysis techniques.

**Implemented ciphers:**

| Cipher | Type |
|---|---|
| Caesar cipher | Shift cipher |
| Affine cipher | Linear substitution |
| Monoalphabetic substitution cipher | Full permutation |
| Vigenère cipher | Polyalphabetic |

The project also includes tools for breaking some of these ciphers using frequency analysis and other cryptanalysis techniques.

---

## 2. How to Run Everything

The program is executed from the command line using:

```bash
python3 crypto.py <command> <action> [options]
```

### 2.1 Caesar Cipher

**Encrypt**

```bash
python3 crypto.py caesar encrypt --key 3 --in message.txt --out cipher.txt
```

**Decrypt**

```bash
python3 crypto.py caesar decrypt --key 3 --in cipher.txt --out message.txt
```

**Breaking**

```bash
python3 crypto.py break caesar --in cipher.txt --lang en
```

> The `--lang` option specifies the language used for frequency analysis.

### 2.2 Affine Cipher

**Encrypt**

```bash
python3 crypto.py affine encrypt --a 5 --b 8 --in message.txt --out cipher.txt
```

**Decrypt**

```bash
python3 crypto.py affine decrypt --a 5 --b 8 --in cipher.txt --out message.txt
```

> The value of `a` must be coprime with 26.

**Breaking**

```bash
python3 crypto.py break affine --in cipher.txt
```

### 2.3 Monoalphabetic Cipher

**Encrypt**

```bash
python3 crypto.py mono encrypt --keyword CRYPTO --in message.txt --out cipher.txt
```

**Decrypt**

```bash
python3 crypto.py mono decrypt --keyword CRYPTO --in cipher.txt --out message.txt
```

> The keyword is used to construct the substitution alphabet.

### 2.4 Vigenère Cipher

**Encrypt**

```bash
python3 crypto.py vigenere encrypt --key LEMON --in message.txt --out cipher.txt
```

**Decrypt**

```bash
python3 crypto.py vigenere decrypt --key LEMON --in cipher.txt --out message.txt
```

**Breaking**

```bash
python3 crypto.py break vigenere --m 5 --in cipher.txt
```

> The `--m` option specifies the assumed length of the Vigenère key.

### 2.5 Input and Output Files

The `--in` option specifies the input file.

The `--out` option is optional. If it is provided, the result is written to that file:

```bash
python3 crypto.py caesar encrypt --key 3 --in message.txt --out cipher.txt
```

If `--out` is not provided, the result is printed directly to the terminal:

```bash
python3 crypto.py caesar decrypt --key 3 --in cipher.txt
```

> Characters that are not part of the alphabet are ignored during encryption and decryption. Therefore, spaces and punctuation are not preserved in their original positions.

---

## 3. Key Space Size of the Four Ciphers

### 3.1 Caesar Cipher

The Caesar Cipher uses a single integer shift over the 26 letters of the alphabet.
Therefore the key space is "26".
The shift of 0 is equal to non encryption, thus, there are 25 keys in reality.

### 3.2 Affine Cipher

This cipher uses 2 parameters, (a,b), the value of b can be any of the 26 alphabet positions.
But, a must be relatively prime to 26 so that a modinv exists.

The total number of possible keys is:

$$12 \times 26 = 312$$

### 3.3 Monoalphabetic Cipher

The monoalphabetic uses a permutation of the 26 letters. Therefore the keyspace is 26!

### 3.4 Vigenère Cipher

This cipher depends directly on the key length.
For example if we have a key length of 5 we have $26^5 = 11.881.376$ different keys in our key space.

---

## 4. C1 — Break Caesar Performance

### 4.1 Measurement Setup

To evaluate the reliability and performance of the Break Caesar frequency based cryptanalysis, two random stories in Spanish and English were generated from which the different length texts came. Each fragment was encrypted using a randomly selected key, and the recovery accuracy (percentage of correctly decrypted keys/texts) was measured across three different scenarios:

1. **Spanish Text and Spanish Frequency Table**
2. **English Text and English Frequency Table**
3. **Spanish Text and English Frequency Table** *(using the wrong table)*

Where the Frequency Tables are the statistical % of appearance of the letters on different languages, saved in frequencies.py.

### 4.2 Data & Results Summary

| Text Length | Spanish | English | ES Text + ENG Table |
|---:|---:|---:|---:|
| **1** | 12.0% | 10.0% | 15.0% |
| **5** | 61.0% | 52.5% | 47.5% |
| **10** | 88.0% | 77.5% | 70.0% |
| **20** | 98.5% | 93.5% | 78.0% |
| **30** | 97.0% | 100.0% | 92.5% |
| **40** | 100.0% | 100.0% | 91.0% |
| **60** | 100.0% | 100.0% | 99.5% |
| **100** | 100.0% | 100.0% | 100.0% |

### 4.3 Analysis

The breaker becomes reliable, let's fix a 90% accuracy to measure that. Thus, it becomes reliable reaching the 20 letter length text in both cases EN and ES.

The wrong table costs that in that 20 letter length the cipher is not reliable with a 78%, we need 30 letters to reach the 90%. Thus, we lose a 1/3 of the capacity to analyze short texts.

---

## 5. C2 — Break Affine Performance

### 5.1 Measurement Setup

Same setup as Caesar's but dealing with a higher key space, from k = n to k = (a,b).

### 5.2 Data & Results Summary

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

### 5.3 Measurements and Analysis

**Number of candidates tested**

For the affine cipher, the breaker tries every combination of a and b. a must be coprime with 26, thus, there are only 12 valid values for a.
This gives us 12 x 26 = 312 candidate keys.

**Shortest reliable length and comparison with C1**

Using the same 90% reliability threshold defined earlier, the affine breaker reaches it at length 30 for ES texts and 40 for ENG texts.
Using the wrong frequency table we can't reach the 90% of reliability until the length of 100.

**Comparison with Caesar's — C1**

The Caesar's breaker reached the 90% with length 20 in both languages, the affine needs higher texts x1.5 and x2 compared with the caesar's.

---

## 6. C3 — Break Vigenère Performance

### 6.1 Measurement Setup

The Vigenère is tested over greater lengths, [60, 120, 200, 300], and with these different lengths we can measure how secure different keys are.

The keys are: 3(HOL), 5(ARIHN), 7(ALEXDFZ) with different lengths each one. Here we can see the complexity of this cipher when the key is longer.

Tested over 200 iterations we measure the different accuracies % in the following table.

### 6.2 Data & Results Summary

**ES**

| Length | HOL (m=3) | ARIHN (m=5) | ALEXDFZ (m=7) |
|---:|---:|---:|---:|
| 60 | 91.5% | 58.5% | 15.0% |
| 120 | 100.0% | 97.0% | 61.5% |
| 200 | 100.0% | 100.0% | 85.5% |
| 300 | 100.0% | 100.0% | 93.0% |

**EN**

| Length | HOL (m=3) | ARIHN (m=5) | ALEXDFZ (m=7) |
|---:|---:|---:|---:|
| 60 | 80.0% | 37.0% | 6.5% |
| 120 | 98.5% | 88.0% | 49.5% |
| 200 | 100.0% | 100.0% | 85.0% |
| 300 | 100.0% | 100.0% | 100.0% |

### 6.3 Measurements and Analysis

What it really matters is not the total length of the ciphered text, instead the sequence length.

$$Subsequence\ length = \frac{ciphertext\_len}{m}$$

The attack divides the text into different sub sequences one for each of the key, and it applies the caesar's individually.

Thats why with length(60) and HOL(m=3) we have subseq of 20 char and gives us a 91% of precision. Otherwise ALEXDFZ(m=7), gives us only 8 to 9 characters and a 15% of precision.

A bigger key makes Vigenère more secure without changing the algorithm because it cut the text in more subsequences, each one shorter. With a long enough key we can stop the attack.

---

## 7. Monoalphabetic Cipher vs AES-128

The key space is not the only thing that matters when we are talking about security.

The monoalphabetic has letter frequencies and has patterns also.

AES-128, despite it has a fewer number of keys (2^128), leaks nothing due to two mechanisms (confusion, diffusion).

Confusion makes the relationship between the key and the text much more complicated and diffusion makes it so that every bit of the original text matters in the cipher.

So brute force is the only option to break the AES-128.

---

## 8. Limitations and Improvements

Some limitations of the implementation are:

- Characters outside the project's alphabet are ignored, so spaces and punctuation are not preserved in the output.
- A possible improvement would be to preserve the original text formatting (spaces, periods, and commas) in the output, instead of only returning the raw sequence of alphabet characters as it currently does.
- Frequency-based cryptanalysis is less reliable on short ciphertexts, since longer ciphertexts provide more reliable statistical information. This affects the Caesar and Affine breakers directly.
- The Vigenère breaker assumes the key length (m) is known or correctly guessed in advance; an incorrect m makes the attack unreliable regardless of ciphertext length.

---

## 9. LLM Usage

Some LLMs as ChatGPT and Claude where used as a support tool, helping with some tasks:

- **Test data generation (ChatGPT):** used to create the `en_text` and `es_text` reference corpora used as input for the breaking tests, lives in breack_caesar_test.py.
- **Documentation formatting (Claude):** used to improve the visual presentation of this `README.md`, without altering its technical content.
- **Code assistance (ChatGPT):** used to help write parts of `crypto.py`, specifically the command-line execution logic.