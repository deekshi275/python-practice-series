def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Args:
        arr: List of comparable elements to be sorted
        
    Returns:
        Sorted list in ascending order
    """
    # Base case: arrays with 0 or 1 element are already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2

    # Recursively sort the left half of the array
    left = merge_sort(arr[:mid])
    # Recursively sort the right half of the array
    right = merge_sort(arr[mid:])

    # Merge the sorted left and right halves back together
    return merge(left, right)


def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
        left: First sorted list
        right: Second sorted list
        
    Returns:
        A single sorted list containing all elements from left and right
    """
    result = []
    # Initialize pointers for both arrays
    i = j = 0

    # Compare elements from left and right arrays and add the smaller one
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add any remaining elements from the left array (if any)
    result.extend(left[i:])
    # Add any remaining elements from the right array (if any)
    result.extend(right[j:])

    return result

# Example usage: Create an unsorted array and sort it using merge sort
arr = [7, 5, 4, 76, 4, 3, 56, 3, 6, 7, 99]
print(merge_sort(arr))



