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

def circular_prime(limit):
    primes = sieve_of_eratosthenes(limit)
    circular = [False] * (limit + 1)
    for idx, prime in enumerate(primes):
        if not prime or circular[idx]:
            continue
        L = str(idx)
        d = len(L)
        L = L*2
        flag = True
        for i in range(d):
            current_num = int(L[i:i+d])
            if not primes[current_num]:
                flag = False
                break
        if flag:
            circular[idx] = True
    return circular

circular = circular_prime(limit)
sum_circular = sum([num for num, circle in enumerate(circular) if circle])
print(sum_circular)