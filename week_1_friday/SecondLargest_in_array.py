# Q-write a program that takes an array and Find Second largest element in an array.

def find_second_largest(arr):
    if len(arr) < 2:
        raise ValueError("Array must contain at least two elements")
    
    first = second = float('-inf')
    
    for number in arr:
        if number > first:
            second = first
            first = number
        elif number > second and number != first:
            second = number
    
    if second == float('-inf'):
        raise ValueError("There is no second largest element")
    
    return second

# Example usage:
arr = [12, 35, 1, 10, 34, 1]
print("Second largest element is:", find_second_largest(arr))
