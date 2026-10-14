# Job Sequencing with Deadlines using Greedy Algorithm

## Objective

Implement the Job Sequencing with Deadlines problem using the Greedy algorithmic paradigm to maximize total earned profit while adhering to individual job execution deadlines.

## Problem Statement

Given a set of $n$ jobs where each job $i$ has an identifier, an integer deadline $d_i$, and an associated profit $p_i$ earned if the job is completed on or before its deadline. Each job takes 1 unit of time to complete, and only one job can be executed on a single resource at any given time unit.

The goal is to determine the optimal job execution sequence that maximizes the total accumulated profit.

## Algorithm

1. Sort all given jobs in descending order of their profit ($p_i$).
2. Identify the maximum deadline among all jobs, say `max_deadline`.
3. Initialize a time slot array of size `max_deadline + 1`, with all slots set to empty (`None`).
4. For each sorted job:
   - Search backwards from its deadline $\min(\text{max\_deadline}, d_i)$ down to 1.
   - If an empty slot $t$ is found, schedule the job in slot $t$, add its profit to `total_profit`, and break to the next job.
5. Return the scheduled sequence and total profit.

## Python Program

The complete implementation is provided in:

`Job_Sequencing_Greedy.ipynb`

### Sample Input

```python
Jobs:
- J1: Deadline = 2, Profit = 100
- J2: Deadline = 1, Profit = 19
- J3: Deadline = 2, Profit = 27
- J4: Deadline = 1, Profit = 25
- J5: Deadline = 3, Profit = 15
```

### Sample Output

```text
=== Job Sequencing Results ===
Jobs: [('J1', 'Deadline: 2', 'Profit: 100'), ('J2', 'Deadline: 1', 'Profit: 19'), ('J3', 'Deadline: 2', 'Profit: 27'), ('J4', 'Deadline: 1', 'Profit: 25'), ('J5', 'Deadline: 3', 'Profit: 15')]
Optimal Execution Order: ['J3', 'J1', 'J5']
Slot Allocation: {1: 'J3', 2: 'J1', 3: 'J5'}
Maximum Total Profit: Rs. 142
```

## Greedy Strategy

- **Greedy Choice Property**: At each step, consider the job yielding the highest profit first.
- **Optimal Substructure**: Placing the highest-profit job in the latest possible valid time slot leaves earlier slots open for jobs with tighter deadlines.

## Time and Space Complexity

- **Time Complexity**:
  - Sorting jobs by profit: $O(n \log n)$
  - Slot allocation: $O(n \times \min(n, \text{max\_deadline}))$
  - Overall Time Complexity: **$O(n^2)$** or **$O(n \log n)$** when using Disjoint Set Union (DSU).
- **Space Complexity**: **$O(n + \text{max\_deadline})$** for slot tracking.

## How to Run

1. Open `Job_Sequencing_Greedy.ipynb` in Jupyter Notebook.
2. Select Python 3 kernel.
3. Run all cells to inspect the greedy scheduling trace.
