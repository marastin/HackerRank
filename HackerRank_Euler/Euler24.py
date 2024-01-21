# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

s = "abcdefghijklm"

max_letter = 13

T = int(input())
for _ in range(T):
    
    n = int(input())
    temp = n
    indices = []
    s_temp = list(s)
    for i in range(max_letter):
        idx = (n-1) // math.factorial(max_letter-1-i)
        n = n % math.factorial(max_letter-1-i)
        indices.append(s_temp[idx])
        s_temp.pop(idx)

    print("".join(indices))