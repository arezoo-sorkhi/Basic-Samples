import numpy as np
import matplotlib.pyplot as plt


# Get user input
num_students = int(input("Enter number of students: "))        # Number of students to simulate
mu_height = float(input("Enter mean height (cm): "))           # Mean height
sigma_height = float(input("Enter standard deviation (cm): ")) # Standard deviation


# Simulate student heights using Gaussian (Normal) distribution
# 'heights' is a NumPy array where each element represents the height of one student
heights = np.random.normal(mu_height, sigma_height, num_students)


# Calculate statistics
# Average height
# Standard deviation
mean_height = np.mean(heights)
std_height = np.std(heights)


# Plot 1: Histogram of heights
plt.figure(figsize=(12,5))

# Left plot: Histogram
plt.subplot(1,2,1)
plt.hist(heights, bins=15, alpha=0.6, color='skyblue', edgecolor='black')
plt.axvline(mean_height, color='red', linestyle='-', label=f'Mean = {mean_height:.2f}')
plt.axvline(mean_height - std_height, color='green', linestyle='--', label=f'Mean - Std = {mean_height - std_height:.2f}')
plt.axvline(mean_height + std_height, color='green', linestyle='--', label=f'Mean + Std = {mean_height + std_height:.2f}')
plt.title("Histogram of Heights")
plt.xlabel("Height (cm)")
plt.ylabel("Number of students")
plt.legend()
plt.grid(True)



# Plot 2: Individual student heights

# Right plot: Individual heights
plt.subplot(1,2,2)
plt.plot(heights, marker='o', linestyle='-', color='blue')
plt.axhline(mean_height, color='red', linestyle='-', label=f'Mean = {mean_height:.2f}')
plt.axhline(mean_height - std_height, color='green', linestyle='--', label=f'Mean - Std = {mean_height - std_height:.2f}')
plt.axhline(mean_height + std_height, color='green', linestyle='--', label=f'Mean + Std = {mean_height + std_height:.2f}')
plt.title("Individual Student Heights")
plt.xlabel("Student Index")
plt.ylabel("Height (cm)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()


# Print statistics in terminal
print("Mean height:", round(mean_height,2))
print("Standard deviation:", round(std_height,2))
