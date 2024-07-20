# Q-write a program that will moves all Zeroes to end of an array
def move_zeroes_to_end(arr):
    n = len(arr)
    if n == 0:
        return arr
    
    # Initialize a pointer for the position to place the next non-zero element
    non_zero_pos = 0

    # Traverse the array
    for i in range(n):
        if arr[i] != 0:
            # Swap the elements
            arr[non_zero_pos], arr[i] = arr[i], arr[non_zero_pos]
            non_zero_pos += 1
    
    return arr

# Example usage:
array = [1, 2, 0, 4, 3, 0, 5, 0]
print("Original array:", array)
result = move_zeroes_to_end(array)
print("Array after moving zeroes to the end:", result)
