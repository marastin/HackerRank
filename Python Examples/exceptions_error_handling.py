
# Doc:
# https://docs.python.org/2/library/exceptions.html#module-exceptions

# Example 1
try:
    print(1/0)
except ZeroDivisionError as e:
    print("Error Code:", e)



# HackerRank
T = int(input())
for _ in range(T):
    try:
        a, b = map(int, input().split())
        print(a//b)
    except Exception as e:
        print("Error Code:", e)


# HackerRank
import re
T = int(input())

for _ in range(T):
    try:
        re.compile(input())
    except Exception:
        print(False)
    else:
        print(True)