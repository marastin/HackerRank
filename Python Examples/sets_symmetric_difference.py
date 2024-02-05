# Example 1
myset = set(['a', 'b']) # Creating a set from a list
myset.add('c')
myset.add((5, 4))
print(myset)

myset.update([1, 2, 3, 4]) # update() only works for iterable objects
print(myset)
myset.discard(10)
myset.remove(4)
# Both the discard() and remove() functions take a single value as an argument
# and removes that value from the set. If that value is not present, discard()
# does nothing, but remove() will raise a KeyError exception.


# Example 2
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}
print(a.union(b)) # Values which exist in a or b
print(a.intersection(b)) # Values which exist in a and b
print(a.difference(b)) # Values which exist in a but not in b
print(a.symmetric_difference(b))


t1 = input()
s1 = set(list(map(int, input().split())))
t2 = input()
s2 = set(list(map(int, input().split())))

lst = sorted(list(s1.union(s2).difference(s1.intersection(s2))))
for item in lst:
    print(item)

