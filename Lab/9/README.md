# 0/1 Knapsack using Branch-and-Bound (LCBB)

## Objective

Implement the 0/1 Knapsack problem using the Least-Cost Branch-and-Bound (LCBB) method with a Priority Queue and dynamic upper bounding to find the exact optimum while pruning sub-optimal search paths.

## Problem Statement

Given $n$ items, each with weight $w_i$ and value $v_i$, and a knapsack of maximum capacity $W$. Determine the subset of items that maximizes the total value without exceeding capacity $W$. Each item can be chosen at most once (0 or 1).

## Branch-and-Bound Technique

Unlike exhaustive brute-force ($O(2^n)$) or standard Dynamic Programming ($O(nW)$ which is pseudo-polynomial), Branch-and-Bound:
1. Calculates an optimistic **Upper Bound** for every subproblem using fractional knapsack greedy completion.
2. Explores the state-space tree by expanding the most promising node first using a max-priority queue (Least-Cost search).
3. **Prunes** (bounds) any child node whose upper bound is less than or equal to the current best known profit (`max_profit`).

## Algorithm

1. Sort all items by value-to-weight ratio in descending order: $v_i / w_i$.
2. Calculate the upper bound of the root state (level 0, weight 0, profit 0).
3. Insert root into a Priority Queue ordered by bound.
4. While the priority queue is not empty:
   - Extract node with highest bound.
   - If node's bound $\le$ `max_profit`, prune it.
   - **Branch 1 (Include next item)**: If new weight $\le W$, update `max_profit` if profit improves, compute bound, and push to queue if bound $>$ `max_profit`.
   - **Branch 2 (Exclude next item)**: Compute bound without this item, and push to queue if bound $>$ `max_profit`.
5. Return `max_profit`.

## Python Program

The implementation is located in:

`Branch_and_Bound_01_Knapsack.ipynb`

### Sample Input

```text
Weights  = [2, 3, 4, 5]
Values   = [3, 4, 5, 6]
Capacity = 5
```

### Sample Output

```text
Nodes Explored: 7
Knapsack Capacity: 5
Weights: [2, 3, 4, 5], Values: [3, 4, 5, 6]
Optimal Value (Branch & Bound): 7
```

## Complexity Analysis

- **Worst-Case Time Complexity**: $O(2^n)$ in pathological inputs.
- **Average-Case Time Complexity**: Significantly faster than DP when $W$ is large, as pruning eliminates large subtrees.
- **Space Complexity**: $O(2^n)$ maximum queue size in worst case, $O(n)$ average.

## How to Run

1. Open `Branch_and_Bound_01_Knapsack.ipynb` in Jupyter Notebook.
2. Select Python 3 kernel.
3. Run all cells to inspect node exploration counts and optimal subset values.
