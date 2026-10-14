# N-Queens Problem using Backtracking

## Objective

Solve the classic $N$-Queens constraint satisfaction puzzle using Depth-First Backtracking with state-space pruning and evaluate its complexity and pruning efficiency.

## Problem Statement

The $N$-Queens problem consists of placing $N$ chess queens on an $N \times N$ chessboard such that no two queens attack each other. This implies:
- No two queens can occupy the same row.
- No two queens can occupy the same column.
- No two queens can share the same positive or negative diagonal.

## Algorithm

1. Place queens row by row, beginning at row 0.
2. Maintain three lookup sets for fast $O(1)$ constraint checking:
   - `cols`: Set of occupied columns.
   - `diag_pos`: Set of occupied $(r + c)$ positive diagonals.
   - `diag_neg`: Set of occupied $(r - c)$ negative diagonals.
3. For row $r$, iterate through column indices $c \in [0, N-1]$:
   - If $c$, $(r + c)$, or $(r - c)$ is in the respective constraint set, prune the branch.
   - Otherwise, place queen at $(r, c)$, update the sets, and recursively call `backtrack(r + 1)`.
   - Upon return, backtrack by unmarking $(r, c)$ from the board and constraint sets.
4. When $r == N$, record the valid board configuration.

## Python Program

The implementation is located in:

`N_Queens_Backtracking.ipynb`

### Sample Output (for $N = 4$)

```text
Total distinct solutions for 4-Queens: 2

--- Solution 1 ---
. Q . .
. . . Q
Q . . .
. . Q .

--- Solution 2 ---
. . Q .
Q . . .
. . . Q
. Q . .
```

## Complexity Analysis

- **State Space**: Without pruning, there are $N^N$ possible configurations.
- **Time Complexity**: **$O(N!)$** with branch-and-bound constraint pruning.
- **Space Complexity**: **$O(N)$** auxiliary stack depth and constraint storage.

## How to Run

1. Open `N_Queens_Backtracking.ipynb` in Jupyter Notebook.
2. Select Python 3 kernel.
3. Run all cells to observe all valid non-attacking placements.
