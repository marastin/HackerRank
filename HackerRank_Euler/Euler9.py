# HackerRank - ProjectEuler+ 9


n = 12
def pythagorean(n):
    ans = []
    for a in range(1, n):
        b = (n**2 - 2 * n * a) / (2 * (n - a))
        if b - int(b) != 0 or b < 1:
            continue
        c = n - a - b
        if a*a + b*b == c*c and b > 0 and c > 0:
            ans.append((a, b, c))
    if ans:
        print(ans)
    return ans

for n in range(100):
    A = pythagorean(n)
    

    abc = -1
    for s in A:
        abc = max(abc, s[0]*s[1]*s[2])
    if abc > 0:
        print(n)
        print(abc)
