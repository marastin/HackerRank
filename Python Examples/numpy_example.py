import numpy as np

# Example 1
print('\n---Example 1---\n')
def arrays(arr):
    return np.array(arr[::-1], dtype=float)

s = '1 2 3 4 -8 -10'
arr = s.strip().split(' ')
result = arrays(arr)
print(result)


# Example 2
print('\n---Example 2---\n')
arr = np.array([1,2,3,4,5,6])
# Using shape to get array dimensions
print(arr.shape)
# Using shape to change array dimensions
arr.shape = (3, 2)
print(arr)


# Example 3
# The reshape tool gives a new shape to an array without changing its data. 
# It creates a new array and does not modify the original array itself.
print('\n---Example 3---\n')
my_array = np.array([1,2,3,4,5,6])
print(np.reshape(my_array,(3,2)), '\n')
print(my_array, '\n')
print(my_array.reshape(2,3), '\n')
print(my_array, '\n')