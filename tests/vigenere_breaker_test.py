import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from break_caesar_test import creator, en_text, es_text
from break_vigenere import break_vigenere
from vigenere import encrypt_vigenere


leng = [60, 120, 200, 300]
keys = ["HOL", "ARIHN", "ALEXDFZ"]
lista_en = creator(en_text,leng)
lista_es= creator(es_text,leng)


def measure():

    for language, text in [("es", es_text), ("en", en_text)]:
        print(language.upper())
        print("--------------------")
        for n in leng:
            print("length:", n)
            for key in keys:
                correct = 0
                for i in range(200):

                    txt = creator(text,leng)
                    encrypted = encrypt_vigenere(txt[n],key)
                    rkey, rtxt = break_vigenere(encrypted,len(key),language)
                    if rkey == key:
                        correct += 1
                    rate = correct / 200 * 100

                print("key:", key,"correct:", rate, "%")
            print(". . . . . . . . . . .")


print(measure())

