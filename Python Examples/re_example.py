import re



# Example 1 - Roman Numbers 1 - 3999
# https://en.wikipedia.org/wiki/Roman_numerals
# https://developers.google.com/edu/python/regular-expressions
S1 = "DXXVIII"
S2 = "DXXVIIII"

pattern = r"^(M{0,3})(C{0,3}|CD|DC{0,3}|CM)(X{0,3}|XL|LX{0,3}|XC)(I{0,3}|IV|VI{0,3}|IX)$"
print(str(bool(re.match(pattern, S1))))
print(str(bool(re.match(pattern, S2))))



# Example 2 - Phone Number
# 10 digits started with 7, 8, 9
pattern = r'^[7-9]\d{9}$'
for _ in range(int(input())):
    t = input()
    if re.match(pattern, t):
        print('YES')
    else:
        print('NO')



# Example 3 - Email
# format: NAME <username@domain.extension>
pattern = r'^\w+\s<[a-zA-Z][\w._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}>$'

n = int(input())
for _ in range(n):
    s = input()
    if re.match(pattern, s):
        print(s)


# Example 4 - Hex Color
pattern = r'(?<!^)(#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)'
# (?: ...) non capturing group
# (?<!x) negative look behind
# ()? zero or one
N = int(input())
for _ in range(N):
    S = input()
    m = re.findall(pattern, S)
    if m:
        for color in m:
            print(color)