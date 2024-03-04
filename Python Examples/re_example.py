import re



# Example 1 - Roman Numbers 1 - 3999
# https://en.wikipedia.org/wiki/Roman_numerals
# https://developers.google.com/edu/python/regular-expressions
S1 = "DXXVIII"
S2 = "DXXVIIII"

pattern = r"^(M{0,3})(C{0,3}|CD|DC{0,3}|CM)(X{0,3}|XL|LX{0,3}|XC)(I{0,3}|IV|VI{0,3}|IX)$"
print(str(bool(re.match(pattern, S1))))
print(str(bool(re.match(pattern, S2))))