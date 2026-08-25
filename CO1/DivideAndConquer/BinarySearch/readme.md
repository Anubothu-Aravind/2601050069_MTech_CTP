# Project: University Library Book Search (Binary Search)

An efficient search implementation to find a book in a sorted database of 10 lakh books.

## 1. Problem Statement
A university library has 1,000,000 (10 lakhs) books arranged in increasing order (e.g., 1, 2, ..., 1,000,000). A student wants to find book number `750000`. Using Binary Search, the system should find and return the exact index/location of this book if present, or output that the book was "Not Found".

## 2. Divide into Parts/Modules
To keep the design clean and modular, the notebook is structured into these logical parts/modules:
* **Core Logic**: A clean, decoupled function containing the primary binary search logic.
* **Data Store & Input Setup**: Sets up the book list database (simulating 10 lakh sorted book IDs) and query parameters.
* **Sample Edge Cases (Test Cases)**: Conceptual descriptions of tests to verify the search logic under extreme conditions.
* **Driver Logic (Main)**: The interactive console driver that accepts dynamic user inputs and runs search queries.

## 3. Abstraction
Abstraction helps focus on essential parameters and hide unnecessary information.

### Needs (Essential Information)
- **List of Book IDs**: A sorted collection of book IDs.
- **Target Book ID**: The specific book ID to search for (`750000`).
- **Control Pointers**: Indices (`low`, `high`, `mid`) to track and halve the search space.

### No Needs (Irrelevant Information)
- Book details (titles, authors, cover design, page counts).
- Physical attributes (shelf rack numbers, library floor).
- Student info (borrower ID, checkout history).

## 4. Algorithm
1. Initialize two pointers: `low = 0` and `high = len(books) - 1`.
2. While `low <= high`:
   a. Compute middle index: `mid = low + (high - low) // 2`.
   b. Compare the element at `mid` with the target:
      - If `books[mid] == target`, return `mid` (Found).
      - If `books[mid] < target`, set `low = mid + 1` (Discard lower half).
      - If `books[mid] > target`, set `high = mid - 1` (Discard upper half).
3. If the loop terminates without finding the target, return `-1` (Not Found).

## 5. Core Logic
```python
def binary_search_books(books, target_id):
    low = 0
    high = len(books) - 1
    
    while low <= high:
        mid = low + (high - low) // 2
        if books[mid] == target_id:
            return mid
        elif books[mid] < target_id:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1
```

## 6. Data Store & Input Setup
```python
# Simulating 1,000,000 sorted books (IDs from 1 to 1,000,000)
books_database = list(range(1, 1000001))
default_target = 750000
```

## 7. Sample Edge Cases (Test Cases)
Here are the test scenarios designed to verify system correctness:

### Test Case 1: Standard Search (Book Found)
* **Input**:
  * `books` = [1, 2, 3, ..., 1000000]
  * `target` = 750000
* **Expected Output**: Book 750000 found at index 749999 (Position 750000)

### Test Case 2: Standard Search (Book Not Found)
* **Input**:
  * `books` = [1, 2, 3, ..., 1000000]
  * `target` = 1500000
* **Expected Output**: Book 1500000 not found (return -1)

### Test Case 3: Empty Database
* **Input**:
  * `books` = []
  * `target` = 5
* **Expected Output**: Book 5 not found (return -1)

### Test Case 4: Single Book Database (Match)
* **Input**:
  * `books` = [42]
  * `target` = 42
* **Expected Output**: Book 42 found at index 0 (Position 1)

### Test Case 5: Single Book Database (No Match)
* **Input**:
  * `books` = [42]
  * `target` = 10
* **Expected Output**: Book 10 not found (return -1)

### Test Case 6: Target at Lower Boundary
* **Input**:
  * `books` = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  * `target` = 1
* **Expected Output**: Book 1 found at index 0 (Position 1)

### Test Case 7: Target at Upper Boundary
* **Input**:
  * `books` = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  * `target` = 10
* **Expected Output**: Book 10 found at index 9 (Position 10)

## 8. Driver Logic (Main)
```python
def interactive_mode():
    """
    Main driver logic that prompts for dynamic input to search for a book.
    """
    try:
        n_input = input("Enter the total number of books in the library [default: 1000000]: ").strip()
        N = int(n_input) if n_input else 1000000
        
        if N < 0:
            print("Error: Number of books cannot be negative.")
            return
            
        print(f"Generating sorted library of {N} books (IDs 1 to {N})...")
        books = list(range(1, N + 1))
        
        target_input = input(f"Enter the book ID to search for (1 to {N}) [default: 750000]: ").strip()
        target = int(target_input) if target_input else 750000
        
        print(f"Searching for book {target} using Binary Search...")
        index = binary_search_books(books, target)
        
        if index != -1:
            print(f"SUCCESS: Book {target} found at index {index} (Position {index + 1} in the sorted list).")
        else:
            print(f"NOT FOUND: Book {target} is not in the library database.")
            
    except ValueError:
        print("Invalid input! Please enter integer values.")

interactive_mode()
```

## Sample Input and Output

### Interactive Dynamic Input Output (Sample Run)
```text
=============================================
        DYNAMIC INPUT / INTERACTIVE MODE
=============================================
Enter the total number of books in the library [default: 1000000]: 1000000
Generating sorted library of 1000000 books (IDs 1 to 1000000)...
Enter the book ID to search for (1 to 1000000) [default: 750000]: 750000
Searching for book 750000 using Binary Search...

SUCCESS: Book 750000 found at index 749999 (Position 750000 in the sorted list).
=============================================
```
