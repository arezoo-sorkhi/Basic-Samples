# Problem Description:

# Write a Python program that counts how many even numbers exist in a list.

#The user enters several integers separated by spaces.
#The program converts the input into a list of integers and then uses a
#function to determine how many of these numbers are even.




# The function must accept a list of integers and return an integer.
from typing import List

def count_even(numbers: List[int]) -> int:
   
    count = 0
    for n in numbers:
        if n % 2 == 0:
            count += 1
    return count


# ------------------- User Input Section -------------------

# Ask user to enter numbers
user_input = input("Please enter several integers separated by spaces: ")

# Convert string input into a list of integers
numbers = list(map(int, user_input.split()))

# Call the function
result = count_even(numbers)

# Display the result
print("Number of even numbers:", result)