def find_max_min(numbers):
    if not numbers:
        return None, None  # Return None for both max and min if the list is empty
    else:
        maximum = max(numbers)
        minimum = min(numbers)
        return maximum, minimum

# Example usage:
my_list = [5, 2, 9, 1, 7, 3]
max_val, min_val = find_max_min(my_list)
print("Maximum value:", max_val)
print("Minimum value:", min_val)
