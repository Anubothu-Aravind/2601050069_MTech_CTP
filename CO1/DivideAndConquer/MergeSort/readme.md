# Project: Student Scholarship Eligibility System (Merge Sort)

An implementation of a stable Merge Sort algorithm in descending order to sort student marks and determine scholarship recipients.

## 1. Problem Statement
Given a database of students with their names and marks:
* Anitha: 95
* Vivek: 83
* Laksmi: 67
* Teja: 97
* Kumar: 85

Sort the list of students in **descending order** of their marks using the **Merge Sort** algorithm, and select the students who are eligible for a scholarship (eligibility threshold: marks $\ge 90$).

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: A stable Merge Sort implementation modified to sort student tuples `(name, marks)` in descending order of marks.
* **Data Store & Input Setup**: Sets up the student database list and scholarship criteria threshold.
* **Sample Edge Cases (Test Cases)**: Conceptual descriptions of tests to verify the sorting logic under different conditions.
* **Driver Logic (Main)**: The interactive console driver that executes the sorting, filters eligible students, and accepts dynamic custom user inputs.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **Student Database**: A list of `(name, marks)` tuples.
- **Scholarship threshold**: The minimum marks required (90).
- **Split and Merge Indexes**: Boundaries (`left`, `right`, `mid`) to track division of subproblems.

### No Needs (Irrelevant Information)
- Student demographic details (roll numbers, address, contact details).
- Enrollment and attendance info.
- Scholarship financial specifics (funding source, award amount).

## 4. Algorithm
1. **Divide**: If the list length is $\le 1$, return it (base case). Otherwise, divide the list into two halves at the midpoint: `mid = len(arr) // 2`.
2. **Conquer**: Recursively apply Merge Sort to the left half and right half.
3. **Combine (Merge)**: Merge the two sorted halves back into a single sorted list in descending order:
   - Compare elements at the pointers of both halves.
   - If the marks of the student in the left half are greater than or equal to the marks of the student in the right half, insert the left student into the temporary list (preserving stability). Otherwise, insert the right student.
   - Copy any remaining students from either half.
4. **Scholarship Filtering**: Traverse the sorted list and select students with `marks >= 90`.

## 5. Core Logic
```python
def merge_sort_students(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_sorted = merge_sort_students(left_half)
    right_sorted = merge_sort_students(right_half)
    merged = []
    i = j = 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i][1] >= right_sorted[j][1]:
            merged.append(left_sorted[i])
            i += 1
        else:
            merged.append(right_sorted[j])
            j += 1

    merged.extend(left_sorted[i:])
    merged.extend(right_sorted[j:])

    return merged
```

## 6. Data Store & Input Setup
```python
students_database = [
    ("Anitha", 95),
    ("Vivek", 83),
    ("Laksmi", 67),
    ("Teja", 97),
    ("Kumar", 85)
]

scholarship_threshold = 90
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Student List (Provided Example)
* **Input**: `[("Anitha", 95), ("Vivek", 83), ("Laksmi", 67), ("Teja", 97), ("Kumar", 85)]`
* **Expected Sorted List**: `[("Teja", 97), ("Anitha", 95), ("Kumar", 85), ("Vivek", 83), ("Laksmi", 67)]`
* **Expected Scholarship Recipients**: `[("Teja", 97), ("Anitha", 95)]`

### Test Case 2: Empty Student List
* **Input**: `[]`
* **Expected Sorted List**: `[]`
* **Expected Scholarship Recipients**: `[]`

### Test Case 3: Single Student List
* **Input**: `[("Anitha", 95)]`
* **Expected Sorted List**: `[("Anitha", 95)]`
* **Expected Scholarship Recipients**: `[("Anitha", 95)]`

### Test Case 4: None Eligible for Scholarship
* **Input**: `[("Vivek", 83), ("Laksmi", 67)]`
* **Expected Sorted List**: `[("Vivek", 83), ("Laksmi", 67)]`
* **Expected Scholarship Recipients**: `[]`

### Test Case 5: Identical Marks (Stability Verification)
* **Input**: `[("StudentA", 90), ("StudentB", 90)]`
* **Expected Sorted List**: `[("StudentA", 90), ("StudentB", 90)]` (preserving original relative order)

## 8. Driver Logic (Main)
To run the driver logic, open the [MergeSort.ipynb](MergeSort.ipynb) notebook and execute the cells.

## Sample Input and Output

### Interactive Output (Sample Run)
```text
=============================================
        Merge Sort - Data
=============================================
Scholarship Threshold: 90
Students in Database:
  - Anitha: 95
  - Vivek: 83
  - Laksmi: 67
  - Teja: 97
  - Kumar: 85
=============================================

Initial Student Database: [('Anitha', 95), ('Vivek', 83), ('Laksmi', 67), ('Teja', 97), ('Kumar', 85)]

Students Sorted in Descending Order of Marks:
  - Teja: 97
  - Anitha: 95
  - Kumar: 85
  - Vivek: 83
  - Laksmi: 67

Scholarship Recipients (Marks >= 90):
  * Teja (97) - ELIGIBLE
  * Anitha (95) - ELIGIBLE
```
