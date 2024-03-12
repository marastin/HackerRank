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


# Example 5 - Check UID for special pattern
# Solution 1
def check_uid(uid):
    # Check for repeating characters
    if len(set(uid)) != len(uid):
        return False
    # Check for at least one uppercase letter
    if not re.search(r'[A-Z].*[A-Z]', uid):
        return False
    # Check for at least three digits
    if len(re.findall(r'\d', uid)) < 3:
        return False
    # Check for alphanumeric characters only
    if not re.match(r'^[a-zA-Z0-9]{10}$', uid):
        return False
    return True


for _ in range(int(input())):
    uid = input()
    print("Valid" if check_uid(uid) else "Invalid")

# Solution 2
pattern = r"^(?!.*(.).*\1)(?=.*[A-Z].*[A-Z])(?=.*\d.*\d.*\d)[A-Za-z0-9]{10}$"

for _ in range(int(input())):
    print("Valid") if re.match(pattern, input()) else print("Invalid")



# Example 6: Card Number
# ► It must start with a 4, 5 or 6.
# ► It must contain exactly 16 digits.
# ► It must only consist of digits (0-9).
# ► It may have digits in groups of 4, separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have 4 or more consecutive repeated digits.
    
pattern = r"^(?!.*(.)(-?\1){3,})([4-6]([0-9]{3})-?([0-9]{4}-?){3})$"
for _ in range(int(input())):
    c = input()
    if re.match(pattern, c):
        print("Valid")
    else:
        print("Invalid")