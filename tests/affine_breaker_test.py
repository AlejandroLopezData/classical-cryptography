import os
import sys
import random
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from break_affine import break_affine
from caesar import encrypt_cesar
from basics import alphabet
from break_caesar_test import creator, en_text,es_text
from affine import encrypt_affine, valid_keys_affine

keys = valid_keys_affine()
leng = [1,5,7,10,20,30,40,60,100]
lista_en = creator(en_text,leng)
lista_es= creator(es_text,leng)



def measure():
    for language, text in [("es", es_text), ("en", en_text), ("en", es_text)]:

        print(language.upper())
        print("--------------------")

        for n in leng:
            correct = 0

            for i in range(200):
                txt = creator(text,leng)
                key = random.choice(keys)

                encrypted = encrypt_affine(txt[n], key[0],key[1])
                rkey,rtxt = break_affine(encrypted, language)

                if rkey == key:
                    correct += 1

            rate = correct / 200 * 100

            print("length:", n, "correct:", rate, "%")

        print()

print(measure())

# works similar in both eng and esp
#in affine we need a bigger txt to be able to decrypt it.
#here we need near to 60 word txt to be close to teh 100% though with 30 letter text we surpass the 90% prob of solving it
# i tested it with more lengths to see how it works in a better perspective


