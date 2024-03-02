import re

# HackerRank
s = 'abaabaabaabaae'
pattern = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[aeouiAEOUI]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'

f = re.findall(pattern, s)
print('\n'.join(f) if f else -1)


# Example 1
print(re.findall(r'\w','http://www.google.com/'))

# Example 2
it = re.finditer(r'\w','http://www.google.com/')
for L in it:
    print(L.group(), end=' ')
print()

# Example 2
it = re.finditer(r'\w','http://www.google.com/')
print(list(map(lambda x: x.group(), it)))
