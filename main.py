# XOR Encryption Algorithm
import random

phrase = input("Enter message to encrypt: ")
phrase_word = []
phrase_ascii = []
phrase_binary = []

for a in phrase:
    phrase_word.append(a)
b = len(phrase_word)

for c in range (0,b):
    phrase_ascii.append(ord(phrase_word[c]))

key = [10000000, 10101010, 11001100, 11110011, 11111100, 10000110]

for d in range (0,b):
    phrase_binary.append(bin(phrase_ascii[d]))

for e in range (0,b):
    split_name_l = []
    split_key_l = []
    cipher = []
    final_cipher = []
    key_final = []
    which_key = random.choice((key))
    which_key = str(which_key)

    first_binary_letter = phrase_binary[e]

    for f in first_binary_letter:
        split_name_l.append(f)

    for g in which_key:
        split_key_l.append(g)

    if split_key_l[0] == split_name_l[0]:
        wow1 = 0
        cipher.append(wow1)

    else:
        yay1 = 1
        cipher.append(yay1)

    for h in range (2, 9):
        if split_key_l[h-1] == split_name_l[h]:
            wow = 0
            cipher.append(wow)
        elif split_key_l[h-1] != split_name_l[h]:
            yay = 1
            cipher.append(yay)

        final_cipher.append(cipher)

    key_final.append(which_key)
    print(f"Cipher Text of letter {e} is {cipher}")
    print(f"Key Used: {key_final}")
