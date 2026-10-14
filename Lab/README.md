# M.Tech Algorithmic Programming & CTP — Laboratory Portfolio

This directory contains the complete set of **13 Laboratory Practical Experiments** implemented for the Master of Technology (M.Tech) Computational Thinking and Programming / Algorithmic Programming course.

Each experiment includes an interactive Jupyter Notebook (`.ipynb`) and comprehensive documentation (`README.md`) covering the problem statement, algorithm design, complexity analysis, and verification.

---

## Master Laboratory Index (Labs 1 to 13)

| Lab # | Experiment Title | Paradigm / Focus | Course Outcome | Experiment Link |
| :---: | :--- | :--- | :---: | :---: |
| **01** | **Merge Sort using Divide-and-Conquer** | Divide & Conquer ($O(n \log n)$) | CO1 | [Lab 01](./1/README.md) |
| **02** | **0/1 Knapsack using Dynamic Programming** | Dynamic Programming (2D Memoization Table) | CO1 | [Lab 02](./2/README.md) |
| **03** | **Stack and Queue using Type Hints & Dataclasses** | Data Structures, Generics & LIFO/FIFO | CO2 | [Lab 03](./3/README.md) |
| **04** | **List-Based vs Generator-Based Processing** | Lazy Evaluation, Memory Profiling & Generators | CO2 | [Lab 04](./4/README.md) |
| **05** | **Banking Management System** | OOP Abstraction, Inheritance & Polymorphism | CO3 | [Lab 05](./5/README.md) |
| **06** | **Student/Employee Data Model using Dataclasses** | Python `@dataclass`, Boilerplate Reduction & Typing | CO3 | [Lab 06](./6/README.md) |
| **07** | **Job Sequencing with Deadlines (Greedy)** | Greedy Method & Profit Maximization | CO1 | [Lab 07](./7/README.md) |
| **08** | **N-Queens Problem using Backtracking** | Backtracking & State-Space Tree Pruning | CO1 | [Lab 08](./8/README.md) |
| **09** | **0/1 Knapsack using Branch-and-Bound (LCBB)** | Least-Cost Branch & Bound with Priority Queue | CO1 | [Lab 09](./9/README.md) |
| **10** | **Trie (Prefix Tree) with Autocomplete** | Pythonic Collections (`defaultdict`) & Trie Search | CO2 | [Lab 10](./10/README.md) |
| **11** | **Design Patterns: Factory and Strategy in Python** | Gang-of-Four (GoF) OOP Patterns & SOLID | CO3 | [Lab 11](./11/README.md) |
| **12** | **Asynchronous I/O and Concurrency (asyncio)** | Event Loops, Coroutines, Rate Limiting & Speedup | CO4 | [Lab 12](./12/README.md) |
| **13** | **Software Quality Engineering (Pytest & Hypothesis)** | Testing Pyramid, Parameterization & Property Testing | CO5 | [Lab 13](./13/README.md) |

---

## Syllabus & Curriculum Alignment

```text
Laboratory Curriculum Matrix:
├── CO1: Algorithmic Thinking & Paradigms   --> Labs 01, 02, 07, 08, 09
├── CO2: Python Data Model & Structures     --> Labs 03, 04, 10
├── CO3: Object-Oriented Engineering       --> Labs 05, 06, 11
├── CO4: Functional Patterns & Concurrency --> Lab 12
└── CO5: Software Quality Engineering      --> Lab 13
```

## How to Execute the Laboratory Notebooks

Each subfolder contains an executable Jupyter notebook. To launch and run all experiments:

```bash
# 1. Start Jupyter from the repository root
jupyter notebook

# 2. Navigate to Lab/<Lab_Number>/ and open the notebook
# 3. Select 'Kernel' -> 'Restart and Run All Cells'
```
