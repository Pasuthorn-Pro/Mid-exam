def find_missing_number(arr: list):
    n = len(arr)
    # Calculate the correct difference using the first two elements
    diff = min(arr[1] - arr[0], arr[2] - arr[1])
    
    for i in range(n - 1):
        if arr[i + 1] - arr[i] != diff:
            return arr[i] + diff
    
    return "no missing"

# Test cases
print(find_missing_number([2, 4, 8, 10]))  # Output: 6
print(find_missing_number([5, 10, 20, 25]))  # Output: 15
print(find_missing_number([1, 3, 5, 9, 11]))  # Output: 7
print(find_missing_number([1, 4, 7, 10, 13]))  # Output: "no missing"
