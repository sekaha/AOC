def find_smallest_greater_or_equal(arr, target):
    left = 0
    right = len(arr) - 1
    result = None

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] >= target:
            result = arr[mid]
            right = mid - 1  # Continue searching on the left side
        else:
            left = mid + 1  # Continue searching on the right side

    return result


sorted_list = [1, 3, 5, 7, 10, 11, 13, 15, 17, 19]
target_value = 8

result = find_smallest_greater_or_equal(sorted_list, target_value)
print(f"The smallest number greater than or equal to {target_value} is: {result}")
