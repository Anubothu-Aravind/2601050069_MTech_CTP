# Merge Sort using Divide-and-Conquer

## Objective

Implement the Merge Sort algorithm using the Divide-and-Conquer technique and analyze its time complexity.

## Algorithm

1. Divide the array into two halves.
2. Recursively sort the left half.
3. Recursively sort the right half.
4. Merge the two sorted halves.
5. Continue until the complete array is sorted.

## Python Program

The Jupyter Notebook `Merge_Sort_Divide_and_Conquer.ipynb` contains the complete Python implementation.

### Sample Input

```text
[38, 27, 43, 3, 9, 82, 10]
```

### Sample Output

```text
Original array:
[38, 27, 43, 3, 9, 82, 10]

Sorted array:
[3, 9, 10, 27, 38, 43, 82]
```

## Divide-and-Conquer

- **Divide:** Split the array into two halves.
- **Conquer:** Recursively sort both halves.
- **Combine:** Merge the two sorted halves.

## Time Complexity

The recurrence relation is:

```text
T(n) = 2T(n/2) + O(n)
```

Therefore:

- Best Case: **O(n log n)**
- Average Case: **O(n log n)**
- Worst Case: **O(n log n)**
- Space Complexity: **O(n)**

## How to Run

1. Open `Merge_Sort_Divide_and_Conquer.ipynb` in Jupyter Notebook or JupyterLab.
2. Select a Python 3 kernel.
3. Run all cells.
