import cmath

# https://docs.python.org/2/library/cmath.html

print(cmath.phase(complex(-1,0)))
print(abs(complex(-1,0)))

c = complex("1+2j")

r = abs(c)
phi = cmath.phase(c)

print(r)
print(phi)

# Using Polar

(r, phi) = cmath.polar(c)
print(r)
print(phi)



