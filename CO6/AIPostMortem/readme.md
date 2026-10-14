# AI Pair Programming Post-Mortem
Reflective analysis of building ~3000 LOC Sudoku project with AI pair tooling.
## Where AI Accelerated
- Boilerplate, type stubs, docstrings, CI/CD YAML
- Test case generation (parametrize, Hypothesis strategies)
## Where AI Failed
- MRV heuristic correctness — manual fix needed
- Context drift across long sessions
- Hallucinated non-existent library APIs
## Reviewer Discipline
- Every function read, understood, and tested before merge
- mypy --strict + ruff on every commit
