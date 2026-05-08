# Create array [10, 20, 30, 40] 
# Find: Sum
# Mean 
# Multiply 
# array by 2 
# Reshape into 2x2
import numpy as np

# Create array
arr = np.array([10, 20, 30, 40])

# Sum
print("Sum:", np.sum(arr))

# Mean
print("Mean:", np.mean(arr))

# Multiply by 2
print("Multiply by 2:", arr * 2)

# Reshape into 2x2
new_arr = arr.reshape(2, 2)
print("Reshaped array:\n", new_arr)