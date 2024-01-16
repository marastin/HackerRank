import random

# Set the limit for prime numbers
limit = 1000000

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

# Generate a boolean list of prime numbers up to the specified limit
prime_numbers_bool = sieve_of_eratosthenes(limit)

# Initialize a list to store cumulative sums of primes
cumulative_sum = [0] * (limit + 1)
temp = 0

# Calculate cumulative sums based on the boolean list of prime numbers
for ind, val in enumerate(prime_numbers_bool):
    if val:
        temp += ind
    cumulative_sum[ind] = temp

# Example: Print the cumulative sum of primes up to index n
n = 100
print(f"Cumulative sum of primes up to index {n}: {cumulative_sum[n]}")


