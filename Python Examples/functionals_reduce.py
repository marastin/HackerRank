from functools import reduce
from math import gcd

print(reduce(lambda x, y : x + y,[1,2,3])) # works the same as sum
print(reduce(gcd, [2,4,8]))
print(reduce(gcd, [2,4,8], 3))

# HackerRank
# from fractions import Fraction
# from functools import reduce

# def product(fracs):
#     t = reduce(lambda x, y: x * y, fracs)
#     return t.numerator, t.denominator

# if __name__ == '__main__':
#     fracs = []
#     for _ in range(int(input())):
#         fracs.append(Fraction(*map(int, input().split())))
#     result = product(fracs)
#     print(*result)