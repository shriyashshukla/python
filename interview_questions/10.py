#What is the difference between del and remove() on lists?

# del is a statement, not a function. It removes the item at a specific index from the list.
# remove() is a function that removes the first occurrence of a specific value from the list.

# del
numbers = [4, 2, 1, 6, 9, 7]
del numbers[0]
print(numbers)
# Output: [2, 1, 6, 9, 7]
# remove()
numbers = [4, 2, 1, 6, 9, 7]
numbers.remove(6)
print(numbers)
# Output: [4, 2, 1, 9, 7]
