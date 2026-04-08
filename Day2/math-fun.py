import numpy as np
arr = np.array([1, 2, 3, 4])

print(np.sum(arr))   # 10
print(np.mean(arr))  # 2.5
print(np.max(arr))   # 4
print(np.min(arr))   # 1

# ==============================================

import numpy as np

arr = np.array([[1, 2], [3, 4]])

print(np.sum(arr))     # 10 (sum of all elements)
print(np.sum(arr, axis=0))  # [4 6] (column sums)
print(np.sum(arr, axis=1))  # [3 7] (row sums)