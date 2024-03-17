import re


# HackerRank
pattern1 = r'(?<=\s)\&\&(?=\s)'
pattern2 = r'(?<=\s)\|\|(?=\s)'

N = int(input())
for n in range(N):
    S = input()
    S = re.sub(pattern1, 'and', S)
    S = re.sub(pattern2, 'or', S)
    print(S)

# Example 1
def square(match):
    number = int(match.group(0))
    return str(number**2)

print(re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9"))



# Example 2
n, m = map(int, input().split())
matrix = [list(input()) for _ in range(n)]
s = "".join(["".join(col) for col in zip(*matrix)])
print(re.sub(r"(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])", " ", s))
    