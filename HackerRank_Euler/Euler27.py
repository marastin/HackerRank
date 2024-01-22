# Set the limit for prime numbers
limit = limit = 2 * 2000 * 2000 + 2000 + 1

# Function to generate a boolean list indicating whether each index is a prime number
def get_primes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    # Mark multiples of each prime as not prime
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num**2, limit + 1, num):
                primes[multiple] = False

    return primes

n = int(input())
limit = limit = 2 * n * n + n + 1

primes = get_primes(limit)

def get_a_b(n, primes=primes):
    max_seq = 0
    a_seq = 0
    b_seq = 0
    for a in range(-n, n):
        for b in range(-n, n):
            for x in range(n+1):
                val = x ** 2 + a * x + b
                if val < 2:
                    break
                if not primes[val]:
                    break
                if x > max_seq:
                    max_seq = x
                    a_seq = a
                    b_seq = b
    return a_seq, b_seq, max_seq



a, b, max_seq = get_a_b(n)
print(f"{a} {b}")
