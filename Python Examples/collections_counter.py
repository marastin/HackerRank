from collections import Counter

# Example 1
myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]

counter = Counter(myList)
print(counter)
print(counter.items())
print(counter.keys())
print(counter.values())


# Example 2
# Original Counter
my_counter = Counter({'a': 2, 'b': 3, 'c': 1})

# Add new items
new_items_to_add = Counter({'b': 2, 'c': 1, 'd': 1})
my_counter.update(new_items_to_add)

# Display the updated Counter
print("Updated Counter (added items):", my_counter)

# Remove items
items_to_remove = Counter({'b': 1, 'c': 1})
my_counter.subtract(items_to_remove)

# Display the updated Counter
print("Updated Counter (removed items):", my_counter)





# Example 3

# Original Counter
my_counter = Counter({'a': 2, 'b': 3, 'c': 1})

# List of elements to update with
elements_to_add = ['b', 'c', 'd', 'b', 'e']

# Update the Counter with the elements from the list
my_counter.update(elements_to_add)

# Display the updated Counter
print("Updated Counter (added elements):", my_counter)

# List of elements to subtract
elements_to_sub = ['b', 'c']

# Update the Counter with the elements from the list
my_counter.subtract(elements_to_sub)

# Display the updated Counter
print("Updated Counter (subtracted elements):", my_counter)




# HackerRank Example

X = int(input())  # number of shoes
N = list(map(int, input().split()))  # all shoe sizes
C = int(input())  # number of customers
R = dict()

counter = Counter(N)
income = 0

for _ in range(C):
    [m, p] = list(map(int, input().split()))
    f = counter[m]
    if f >= 1:
        counter.subtract([m])
        income += p
        
print(income)