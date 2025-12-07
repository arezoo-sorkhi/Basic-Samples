"""
NumPy & Matplotlib 
Compute the mean and variance of a list of numbers and visualize them.
"""

import numpy as np
import matplotlib.pyplot as plt

# 1️⃣ List of numbers
numbers = [2, 4, 6, 8]

# 2️⃣ Convert to NumPy array
arr = np.array(numbers)

# 3️⃣ Compute mean and variance
mean = np.mean(arr)
variance = np.var(arr)

# 4️⃣ Print results
print("Numbers:", numbers)
print("Mean:", mean)
print("Variance:", variance)


plt.figure(figsize=(6, 4))
plt.plot(arr, marker='o', linestyle='-', color='blue', label='Numbers')
plt.axhline(mean, color='red', linestyle='--', label=f'Mean = {mean}')
plt.title("Numbers and Their Mean")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()