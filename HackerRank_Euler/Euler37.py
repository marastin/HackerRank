# Enter your code here. Read input from STDIN. Print output to STDOUT
# Set the limit for prime numbers
limit = int(input())

# Function to generate a boolean list indicating whether each index is a prime number
def sieve_of_eratosthenes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    # Mark multiples of each prime as not prime
    for num in range(2, int(limit**0.5) + 1):
        if primes[num]:
            for multiple in range(num**2, limit + 1, num):
                primes[multiple] = False

    return primes


def is_truncatable(num, primes):
    pass


primes = sieve_of_eratosthenes(limit)

s = 0
t1 = []
t2 = []
t1.append([2, 3, 5, 7])
for i in range(6):
    t1.append([p*10 + q for p in t1[i] for q in range(10) if (p*10 + q) <= limit and primes[p*10 + q]])
    
    for n in t1[i]:
        if n > 10 and primes[(n % 10)] and primes[(n % 100)] and primes[(n % 1000)] and primes[(n % 10000)] and primes[(n % 100000)]:
            t2.append(n)
    
s += sum(t2)



print(s)

