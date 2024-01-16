"""This code is designed to efficiently find the first triangular number with a specified number of factors. 
It utilizes the coprimality of consecutive triangular numbers and the prime factorization properties to optimize 
the calculation of the number of divisors. The find_triangular_with_factors function iterates through triangular 
numbers until it finds one with the desired number of factors, and it then displays the result for each test case.
"""
# Method 1

# def find_factors(number):
#     factors = []
#     for i in range(1, number + 1):
#         if number % i == 0:
#             factors.append(i)
#     return factors

# n = 3
# num_factors = 0
# ind = 1
# while num_factors < n + 1:
#     tri = int(ind * (ind + 1) / 2)
#     num_factors = len(find_factors(tri))
#     ind += 1
# print(tri)




# Method 2
# def count_factors(num):
#     count = 1
#     i = 2
#     while i * i <= num:
#         power = 0
#         while num % i == 0:
#             num //= i
#             power += 1
#         count *= (power + 1)
#         i += 1
#     if num > 1:
#         count *= 2
#     return count

# def find_triangular_with_factors(n):
#     ind = 1
#     tri = 1
#     while count_factors(tri) <= n:
#         ind += 1
#         tri += ind
#     return tri



# Method 3 - 
def count_factors(num):
    # Function to count the number of divisors for a given number
    count = 1
    i = 2
    while i * i <= num:
        power = 0
        while num % i == 0:
            num //= i
            power += 1
        count *= (power + 1)
        i += 1
    if num > 1:
        count *= 2
    return count

def find_triangular_with_factors(n):
    # Function to find the first triangular number with at least 'n' factors
    ind = 1
    while True:
        # Calculate the number of divisors for T_n and T_{n+1} based on even or odd index
        if ind % 2 == 0:
            count1 = count_factors(ind // 2)
            count2 = count_factors(ind + 1)
        else:
            count1 = count_factors(ind)
            count2 = count_factors((ind + 1) // 2)
        
        # Calculate the total number of divisors for T_n * T_{n+1}
        total_factors = count1 * count2
        
        # Check if the total number of divisors exceeds the specified threshold 'n'
        if total_factors > n:
            return ind * (ind + 1) // 2
        
        # Move to the next triangular number
        ind += 1

# Input: Number of test cases
t = int(input("Enter the number of test cases: "))

# Process each test case
for _ in range(t):
    # Input: Desired number of factors
    n = int(input("Enter the desired number of factors: "))
    
    # Find and display the first triangular number with at least 'n' factors
    result = find_triangular_with_factors(n)
    print(f"The first triangular number with {n} factors is: {result}")

