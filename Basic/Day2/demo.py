import numpy as np
print(np.array([1,2,3]))


# ================---Generate Arrays

print(np.zeros((2, 3)))   # all zeros
print(np.ones((2, 2)))    # all ones
print(np.arange(1, 10))   # 1 to 9




# -=======================Reshape Array
arr = np.array([1,2,3,4,5,6])

new_arr = arr.reshape(2, 3)
print(new_arr)  # 2 rows and 3 columns


# ==============================================

import numpy as np

arr = np.array([[1, 2], [3, 4]])

print(arr.shape)   # rows & columns
print(arr.size)    # total elements
print(arr.dtype)   # data type


# ========================

import numpy as np

arr = np.array([1, 2, 3, 4])

print(np.sum(arr))   # 10
print(np.mean(arr))  # 2.5
print(np.max(arr))   # 4
print(np.min(arr))   # 1


# ======================Indexing & Slicing

arr = np.array([10, 20, 30, 40])

print(arr[0])      # 10
print(arr[1:3])    # [20 30]