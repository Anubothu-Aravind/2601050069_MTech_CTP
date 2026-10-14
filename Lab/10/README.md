# Trie (Prefix Tree) with Autocomplete

## Objective

Develop an efficient, Pythonic Trie (Prefix Tree) implementing insertion, exact search, prefix matching, and frequency-ranked autocomplete suggestions using Python's `collections.defaultdict` and strict type hints.

## Problem Statement

Search engines, code editors, and mobile keyboards require instant retrieval of words matching a given prefix. Standard array lookups require $O(N \cdot L)$ time where $N$ is vocabulary size and $L$ is word length. A Trie achieves $O(L)$ query time independent of the total dictionary size.

## Trie Structure & Pythonic Features

- **Recursive Node Definition**: Uses `collections.defaultdict(TrieNode)` for clean, lazy child node instantiation without repetitive `if char not in children:` checks (idiomatic EAFP).
- **Type Annotations**: Adheres to modern Python type hint standards (`Dict[str, 'TrieNode']`, `List[str]`).
- **Terminal Marker & Frequency**: Tracks whether a node terminates a valid word and records word search frequency to rank autocomplete recommendations.

## Algorithm

### Insertion
1. Start at root node.
2. For each character in the word, traverse or dynamically create child node.
3. At the final character, set `is_terminal = True` and increment `frequency`.

### Autocomplete
1. Traverse down to the node representing the target prefix.
2. If prefix does not exist, return an empty list.
3. Perform a Depth-First Search (DFS) from the prefix node to gather all reachable words and their frequencies.
4. Sort matching words by frequency descending and return the top $K$ results.

## Python Program

The implementation is located in:

`Trie_Autocomplete_Collections.ipynb`

### Sample Output

```text
Search 'apple': True
Search 'apply': False
Starts with 'app': True
Autocomplete suggestions for 'app': ['app', 'application', 'apple']
Autocomplete suggestions for 'ban': ['band', 'bandage', 'banana']
```

## Time and Space Complexity

| Operation | Time Complexity | Auxiliary Space |
|---|---|---|
| Insert Word (length $L$) | $O(L)$ | $O(L)$ |
| Search Word (length $L$) | $O(L)$ | $O(1)$ |
| Starts With (prefix length $P$) | $O(P)$ | $O(1)$ |
| Autocomplete | $O(P + K \log K)$ | $O(\text{subtree size})$ |

Total Space Complexity: $O(\Sigma \cdot L \cdot N)$ where $\Sigma$ is alphabet size, $L$ is average word length, and $N$ is number of keys.

## How to Run

1. Open `Trie_Autocomplete_Collections.ipynb` in Jupyter Notebook.
2. Select Python 3 kernel.
3. Run all cells to verify lookup correctness and autocomplete ranking.
