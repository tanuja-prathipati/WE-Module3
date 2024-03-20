def distribute_idlis_optimized(idlis):
    n = len(idlis)
    total_additional_idlis = 0
    # Iterate through the list of idlis
    for i in range(n):
        # Calculate the additional idlis needed to make the count even
        additional_idlis_needed = (idlis[i] % 2)
        # Add additional idlis to the current person
        idlis[i] += additional_idlis_needed
        total_additional_idlis += additional_idlis_needed
        # If the current person needed an additional idli and there's a person behind, distribute one idli
        if additional_idlis_needed and i < n - 1:
            idlis[i+1] += 1
            total_additional_idlis += 1
    # Check if the total number of idlis is even
    if sum(idlis) % 2 != 0:
        return -1
    else:
        return total_additional_idlis

# Test cases
test_cases = [
    [2, 4, 6, 8],
    [1, 3, 5, 7],
    [2, 4, 6, 7],
    [1, 4, 6, 8]
]

for i, idlis in enumerate(test_cases, 1):
    result = distribute_idlis_optimized(idlis)
    if result != -1:
        print(f"Test Case {i}: Minimum idlis distributed: {result}")
    else:
        print(f"Test Case {i}: Distribution not possible.")
