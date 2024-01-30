#!/bin/python3

import sys

def sum_multiples_of_3_or_5(N):
    N -= 1  # Adjust N to exclude itself from the range
    sum_divisible_by = lambda x: x * (N // x) * (N // x + 1) // 2  # Arithmetic series sum formula

    sum_3 = sum_divisible_by(3)
    sum_5 = sum_divisible_by(5)
    sum_15 = sum_divisible_by(15)  # To avoid double counting (multiples of both 3 and 5)

    return sum_3 + sum_5 - sum_15
    
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    # print(int(sum_multiples_of_3_or_5(n)))
    
    n_3 = (n-1)//3
    n_5 = (n-1)//5
    n_15 = (n-1)//15
    
    s_3 = 3*n_3*(n_3 + 1)//2
    s_5 = 5*n_5*(n_5 + 1)//2
    s_15 = 15*n_15*(n_15 + 1)//2
    print(int(s_3 + s_5 - s_15))