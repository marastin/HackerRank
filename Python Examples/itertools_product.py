# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import product

A = list(map(int, input().split()))
B = list(map(int, input().split()))

P = product(A, B)

for item in P:
    print(item, end=' ')




# Some examples:
print(list(product([1,2,3],repeat = 2)))

print(list(product([1,2,3],[3,4])))

A = [[1,2,3],[3,4,5]]
print(list(product(*A)))

B = [[1,2,3],[3,4,5],[7,8]]
print(list(product(*B)))