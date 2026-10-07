# List vs Generator Processing in Python

## Problem Statement

A university needs to process the marks of **1,000,000 students** to identify students who scored above a specified threshold.

The development team wants to compare conventional **list-based processing** with **generator-based processing** to determine their performance and memory requirements.

### Task

Implement two Python solutions:

1. Use a **list** to generate and store all processed results.
2. Use a **generator** to produce the results lazily.

Compare both approaches based on:

- Execution time
- Memory consumption
- Number of elements processed

Display the results and explain why generator-based processing can reduce memory usage.

---

## Approach

### 1. List-Based Processing

The list-based approach uses a list comprehension to find all marks above the threshold.

```python
def list_based(marks):
    return [mark for mark in marks if mark > threshold]
```

All matching results are stored in memory at the same time.

---

### 2. Generator-Based Processing

The generator-based approach uses `yield` to produce matching marks one at a time.

```python
def generator_based(marks):
    for mark in marks:
        if mark > threshold:
            yield mark
```

The results are generated lazily, so they do not all need to be stored in memory.

---

## Sample Data

```python
N = 1_000_000
threshold = 75
marks = [i % 101 for i in range(N)]
```

### Explanation

- `N = 1_000_000` represents one million students.
- The expression `i % 101` generates marks from **0 to 100 repeatedly**.
- The condition `mark > 75` selects students who scored above the threshold.

---

## Performance Comparison

### Example Output

```text
List-based processing:
Number of elements processed: 247524
Execution time: 0.021045 seconds
Peak additional memory: 1.98 MB

Generator-based processing:
Number of elements processed: 247524
Execution time: 0.053249 seconds
Peak additional memory: 0.35 MB
```

> **Note:** The exact execution time and memory usage may vary depending on the computer and Python environment.

---

## Result Analysis

Both approaches produce the same number of qualifying students because they use the same input marks and the same filtering condition.

### List-Based Approach

- Generally faster in this example.
- Stores all matching results in memory.
- Requires more memory as the number of results increases.

### Generator-Based Approach

- Produces results lazily, one at a time.
- Does not store all matching results simultaneously.
- Uses significantly less additional memory.
- May be slightly slower because values are generated on demand.

Therefore, generators are useful when working with **very large amounts of data** where reducing memory consumption is important.

---

## Memory Comparison

| Feature | List | Generator |
|---|---|---|
| Processing | Eager | Lazy |
| Results stored | All results | One result at a time |
| Memory usage | Higher | Lower |
| Execution speed | Usually faster | May be slower |
| Reusable | Yes | No, once exhausted |
| Suitable for | Smaller datasets | Large/streaming datasets |

---

## Why Do Generators Use Less Memory?

A list stores every matching element in memory:

```text
Input Data
    ↓
Filter
    ↓
[76, 77, 78, 79, ...]
    ↓
All results stored in memory
```

A generator produces each result only when it is requested:

```text
Input Data
    ↓
Filter
    ↓
76 → process
77 → process
78 → process
79 → process
...
```

The generator does not need to maintain the complete collection of matching results in memory.

---

## Viva Questions and Answers

### 1. Why is `tracemalloc` used?

`tracemalloc` is used to measure the memory used by the Python program during execution. It helps us compare the memory consumption of the list and generator approaches.

### 2. What does `i % 101` do?

`i % 101` generates values from **0 to 100 repeatedly**. It is used to simulate marks for 1,000,000 students.

### 3. Why use a generator instead of a list?

A generator produces results one at a time instead of storing all results in memory. Therefore, it generally uses less memory.

### 4. What is the difference between `return` and `yield`?

`return` gives the complete result and ends the function.

`yield` produces one result at a time and pauses the function, allowing it to continue later.

### 5. Can a generator be reused after it is exhausted?

No. Once a generator has produced all its values, it is exhausted. To use the values again, a new generator must be created.

---

