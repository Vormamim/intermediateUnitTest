def calculate_sum(f,g):
    return f+g

def highest_duplicate_number(arr):
    # Initialize a set to keep track of numbers seen so far
    seen = set()

    # Initialize a variable to keep track of the highest duplicate number found
    highest_duplicate = -1

    # Iterate over the array
    for num in arr:
        # Check if the number has already been seen
        if num in seen:
            # If the number is a duplicate and higher than the current highest duplicate,
            # update the highest duplicate
            if num > highest_duplicate:
                highest_duplicate = num
        else:
            # Add the number to the set of seen numbers
            seen.add(num)

    # Return the highest duplicate number found
    return highest_duplicate
