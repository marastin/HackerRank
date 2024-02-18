# https://docs.python.org/2/library/collections.html#deque-objects

from collections import deque
import itertools

# deque Recipes

def tail(filename, n=10):
    'Return the last n lines of a file'
    return deque(open(filename), n)


# Another approach to using deques is to maintain a sequence of recently added elements by appending
# to the right and popping to the left:
def moving_average(iterable, n=3):
    # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
    # http://en.wikipedia.org/wiki/Moving_average
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1))
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft()
        d.append(elem)
        yield s / float(n)



# HackerRank
T = int(input())

d = deque()
for _ in range(T):
    s = input().split()
    if s[0] == 'append':
        d.append(int(s[1]))
    elif s[0] == 'appendleft':
        d.appendleft(int(s[1]))
    elif s[0] == 'pop':
        d.pop()
    elif s[0] == 'popleft':
        d.popleft()

print(*d)