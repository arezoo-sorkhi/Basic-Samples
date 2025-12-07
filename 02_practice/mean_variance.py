"""
Problem Description:
--------------------
Write a small Python program that computes the mean and variance of a list of numbers.

The user enters several numbers separated by spaces.
The program converts this input into a list of floats and then uses two separate functions
to calculate the mean and the variance.

"""

from typing import List


def compute_mean(numbers: List[float]) -> float:
    """
    Computes the mean (average) of a list of numbers.
    Formula: mean = sum(numbers) / len(numbers)
    """
    return sum(numbers) / len(numbers)


def compute_variance(numbers: List[float]) -> float:
    """
    Computes the variance of a list of numbers.
    Formula: variance = sum((x - mean)^2 for x in numbers) / len(numbers)
    """
    mean = compute_mean(numbers)
    squared_diffs = [(x - mean) ** 2 for x in numbers]
    return sum(squared_diffs) / len(numbers)


# --------- User Input Section ---------

user_input = input("Please enter several numbers separated by spaces: ")

# Convert string into a list of floats
numbers = list(map(float, user_input.split()))

# Compute results
mean_value = compute_mean(numbers)
variance_value = compute_variance(numbers)

# Print results
print("Mean:", mean_value)
print("Variance:", variance_value)