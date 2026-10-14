# Software Quality Engineering with Pytest and Hypothesis

## Objective

Demonstrate enterprise-grade Software Quality Engineering practices in Python, covering:
- Unit testing with Pytest
- Parameterized test cases (`@pytest.mark.parametrize`)
- Test fixtures for reusable state
- Property-based invariant testing with Hypothesis
- Code coverage analysis and regression prevention

## Problem Statement

Writing standard test cases only evaluates specific predetermined inputs (happy paths and anticipated corner cases). In critical algorithmic systems, unforeseen edge cases (empty inputs, large inputs, negative values, duplicates) often trigger production bugs. Combining standard unit test suites with **Property-Based Testing (Hypothesis)** ensures algorithms satisfy mathematical invariants across thousands of randomized inputs.

## Quality Engineering Methodologies

1. **Testing Pyramid**:
   - **Unit Tests**: Rapid, isolated validation of core functions (e.g. `binary_search`).
   - **Parameterized Testing**: Running the same test logic against a matrix of varied input/output tuples.
   - **Property-Based Testing**: Instead of testing $f(x) == y$, assert system properties such as:
     - *Completeness*: If $x \in S$, then $\text{search}(S, x) \ge 0$.
     - *Soundness*: If $\text{search}(S, x) = i$, then $S[i] == x$.
     - *Monotonicity*: If $x \notin S$, then $\text{search}(S, x) == -1$.
2. **Defensive Invariant Checking**: Validates pre-conditions and post-conditions.

## Python Program

The implementation is located in:

`Software_Testing_Pytest_Hypothesis.ipynb`

### Sample Output

```text
==================================================
        SOFTWARE QUALITY SUITE EXECUTION
==================================================
Running Unit Tests:
- test_binary_search_found: PASSED
- test_binary_search_not_found: PASSED
- test_binary_search_empty: PASSED

Running Property-Based Invariant Verification:
- Tested 5 randomized array invariants with varying sizes and distributions.
- Invariant 1 (Membership Preservation): PASSED
- Invariant 2 (Soundness of Found Index): PASSED
- Invariant 3 (Absence Verification): PASSED

All unit tests and property-based invariant checks passed successfully!
Pytest fixtures, parameterization, and Hypothesis invariant testing validated.
==================================================
```

## Testing Comparison

| Feature | Standard Unit Testing | Property-Based Testing (Hypothesis) |
|---|---|---|
| Input Source | Hardcoded by engineer | Auto-generated pseudo-randomly |
| Coverage | Known scenarios | Discovers unknown edge-cases & shrinks failures |
| Maintenance | High (write many tests) | Low (write invariants, engine tests hundreds) |
| Bug Detection | Good for regression | Excellent for boundary conditions |

## How to Run

1. Open `Software_Testing_Pytest_Hypothesis.ipynb` in Jupyter Notebook.
2. Select Python 3 kernel.
3. Run all cells to verify unit test assertions and property invariant validation.
