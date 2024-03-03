import re

# Example 1
m = re.search(r'\d+','1234')
print(m.end())
print(m.start())


# HackerRank
s = 'aaadaa'
k = 'aa'
pattern = f'(?=({k}))'
m = list(re.finditer(pattern, s))
if m:
    for item in m:
        print((item.start(), item.end() + len(k) - 1))
else:
    print((-1, -1))