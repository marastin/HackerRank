coins = [1, 2, 5, 10, 20, 50, 100, 200]

def count_combinations(coins, n):
    comb = [0]*(n+1)
    comb[0] = 1

    for coin in coins:
        for i in range(coin, n+1):
            comb[i] += comb[i-coin]
    
    return comb

T = int(input())

n = []
for _ in range(T):
    n.append(int(input()))

comb = count_combinations(coins, max(n))

for idx in n:
    print(comb[idx] % (10**9+7))