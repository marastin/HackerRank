# Enter your code here. Read input from STDIN. Print output to STDOUT
import string
from itertools import product

lowercase_letters = [ord(char) for char in string.ascii_lowercase]  # (a-z)
uppercase_letters = [ord(char) for char in string.ascii_uppercase]  # (A-Z)
digits = [ord(char) for char in string.digits]  # (0-9)
other_characters = ['(', ')', ';', ':', ',', '.', "'", '?', '-', '!', ' ']
other_characters_with_ascii = [ord(char) for char in other_characters]

all_ascii_codes = lowercase_letters + uppercase_letters + digits + other_characters_with_ascii

possible_keys = product(lowercase_letters, repeat=3)

n = int(input())
text = list(map(int, input().split()))

key_ok = False
for key in possible_keys:
    for idx in range(n):
        if text[idx] ^ key[idx % len(key)] not in all_ascii_codes:
            key_ok = False
            break
        key_ok = True
    if key_ok:
        break
print("".join(list(map(chr, key))))
