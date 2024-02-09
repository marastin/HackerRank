A = set(map(int, input().split()))

n = int(input())
is_strict_superset = True
for _ in range(n):
    N = set(map(int, input().split()))
    if len(N) == len(A) or (A & N) != N:
        is_strict_superset = False
        break

print(is_strict_superset)