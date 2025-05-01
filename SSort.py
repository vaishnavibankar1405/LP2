def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        # Assume the current position has the smallest value
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap the found minimum element with the current element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Input array
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Sorting the array
selection_sort(arr)

# Output the sorted array
print("Sorted array:", arr)
