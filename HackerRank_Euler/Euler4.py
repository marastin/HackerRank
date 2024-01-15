# LCM : Least Common Multiple (K-M-M)
# GCD : Greatest Common Divisor


n = 10

def gcd(a,b): # Greatest common divisor
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return a*b/gcd(a,b)

lcm_total = 1

for i in range(2, n+1):
    lcm_total = lcm(i, lcm_total)

print(lcm_total)
print(gcd(100,8))
print(lcm(100,8))
