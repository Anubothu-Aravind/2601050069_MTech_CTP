# 0/1 Knapsack using Dynamic Programming

## Objective

Implement the 0/1 Knapsack problem using Dynamic Programming and analyze its time and space complexity.

## Problem Statement

Given `n` items, each item has a weight and a value. A knapsack has a maximum capacity `W`.

The objective is to select items so that:

- The total weight does not exceed the capacity.
- The total value is maximum.
- Each item can be selected at most once.

## Algorithm

Let `dp[i][w]` represent the maximum value that can be obtained using the first `i` items with a knapsack capacity of `w`.

1. Create a DP table of size `(n + 1) x (W + 1)`.
2. Initialize the first row and first column to `0`.
3. Consider each item one by one.
4. If the item's weight is greater than the current capacity, do not select it.
5. Otherwise, choose the maximum value between:
   - Excluding the current item.
   - Including the current item.
6. The final answer is `dp[n][W]`.

## Recurrence Relation

If the current item's weight is greater than the current capacity:

```text
dp[i][w] = dp[i-1][w]
```

Otherwise:

```text
dp[i][w] = max(
    dp[i-1][w],
    value[i-1] + dp[i-1][w-weight[i-1]]
)
```

## Input Used

```text
Weights  = [2, 3, 4, 5]
Values   = [3, 4, 5, 6]
Capacity = 5
```

## Output

```text
Weights: [2, 3, 4, 5]
Values: [3, 4, 5, 6]
Knapsack Capacity: 5
Maximum Value: 7
```

The optimal selection is:

```text
Item 1: Weight = 2, Value = 3
Item 2: Weight = 3, Value = 4

Total Weight = 5
Total Value = 7
```

## Time Complexity

The DP table contains approximately `n x W` entries, and each entry takes constant time to calculate.

Therefore:

**Time Complexity = O(nW)**

where:
- `n` = number of items
- `W` = knapsack capacity

## Space Complexity

A two-dimensional DP table of size `(n + 1) x (W + 1)` is used.

Therefore:

**Space Complexity = O(nW)**

## Complexity Summary

| Property | Complexity |
|---|---|
| Technique | Dynamic Programming |
| Time Complexity | O(nW) |
| Space Complexity | O(nW) |
| Type | 0/1 Knapsack |
| Item Selection | Each item at most once |

## Important Note

The `O(nW)` running time is called **pseudo-polynomial** because it depends on the numerical value of the capacity `W`, rather than only on the length of the input.
