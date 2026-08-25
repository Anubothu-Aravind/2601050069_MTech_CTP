# Merge Sort

A classic sorting algorithm that utilizes the Divide and Conquer paradigm to sort an array.

## Introduction
Merge Sort is a sorting algorithm based on the Divide and Conquer paradigm. It works by recursively dividing the unsorted list into $N$ sublists, each containing one element (a list of one element is considered sorted), and then repeatedly merging sublists to produce new sorted sublists until there is only one sublist remaining.

## Why/Where it is Used
Merge Sort is popular because it guarantees a worst-case time complexity of $O(N \log N)$ and is a stable sort. It is used in:
- Sorting linked lists (since it doesn't require random access memory).
- External sorting (when the dataset is too large to fit in RAM and must be sorted from external storage like hard drives).
- E-commerce applications where stability is important (retaining the original relative order of items with equal keys).

## Problem Statement
Given an unsorted array of $N$ elements, sort it in ascending order.

## Abstraction
Merge Sort abstracts sorting by breaking down a large, complex sorting problem into smaller, trivial subproblems (sorting lists of size 1) and then combining the sorted parts. The core abstraction lies in the `merge` function, which takes two sorted sublists and combines them into a single sorted list.

## Edge Cases
- **Empty Array**: The array contains no elements (returns empty array).
- **Single Element**: The array contains one element (already sorted).
- **Already Sorted**: The array is already in ascending order.
- **Reverse Sorted**: The array is in descending order.
- **Duplicate Elements**: The array contains multiple occurrences of identical elements (Merge Sort preserves their relative order due to stability).

## Algorithm/Steps
1. If the array length is 1 or less, return the array (base case).
2. Divide the unsorted array into two halves at the midpoint: `mid = len(arr) // 2`.
3. Recursively apply Merge Sort to the left half and the right half.
4. Merge the two sorted halves back into a single sorted array by comparing elements pointer-by-pointer.

## Complexity
- **Time Complexity**:
  - **Best Case**: $O(N \log N)$
  - **Average Case**: $O(N \log N)$
  - **Worst Case**: $O(N \log N)$
- **Space Complexity**: $O(N)$ (requires auxiliary space to store the divided subarrays during the merge process).

## Python Implementation
```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive calls
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge step
        i = j = k = 0

        # Copy data to temp arrays
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
```

## Sample Input/Output
### Sample 1
- **Input**: `[12, 11, 13, 5, 6, 7]`
- **Output**: `[5, 6, 7, 11, 12, 13]`

### Sample 2
- **Input**: `[5, 2, 9, 1, 5, 6]`
- **Output**: `[1, 2, 5, 5, 6, 9]`
