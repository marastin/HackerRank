import numpy as np

# Example 1
def arrays(arr):
    return np.array(arr[::-1], dtype=float)

s = '1 2 3 4 -8 -10'
arr = s.strip().split(' ')
result = arrays(arr)
print(result)


# Example 2
arr = np.array([1,2,3,4,5,6])
# Using shape to get array dimensions
print(arr.shape)
# Using shape to change array dimensions
arr.shape = (3, 2)
print(arr)