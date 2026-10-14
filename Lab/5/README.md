# Banking Management System

## Objective

Design and implement a robust Banking Management System demonstrating Object-Oriented Programming (OOP) principles in Python, including:
- Abstraction
- Inheritance
- Polymorphism
- Encapsulation
- Dataclasses and Type Hints

## Problem Statement

A banking institution requires an automated account management system to handle customer accounts, deposits, withdrawals, balance checks, and account statements. The system must support different account types (such as Savings Accounts with minimum balance rules and Current Accounts with overdraft allowances) while enforcing strict input validation and domain constraints.

## Architecture & Class Hierarchy

1. **`Account` (Abstract Base Class)**: Defines the common interface and shared properties (account number, account holder name, balance).
2. **`SavingsAccount`**: Inherits from `Account`, enforces a minimum balance requirement, and calculates periodic interest.
3. **`CurrentAccount`**: Inherits from `Account`, allows an overdraft limit for business transactions.
4. **`Bank`**: Aggregates and manages multiple accounts, supporting account opening, funds transfer between accounts, and account lookups.

## Algorithm

### Deposit Operation
1. Accept account number and deposit amount.
2. Verify amount is strictly positive ($> 0$).
3. Add amount to current balance and log transaction.
4. Return updated balance.

### Withdrawal Operation
1. Accept account number and withdrawal amount.
2. Verify amount is strictly positive ($> 0$).
3. Check balance constraints:
   - For `SavingsAccount`: ensure `balance - amount >= minimum_balance`.
   - For `CurrentAccount`: ensure `balance - amount >= -overdraft_limit`.
4. Deduct amount, log transaction, and return updated balance.

## Python Program

The complete implementation and interactive demonstration is available in:

`Banking_Management_System.ipynb`

## Sample Output

```text
==================================================
           BANKING MANAGEMENT SYSTEM
==================================================
Created Savings Account: SB1001 for Aravind (Initial: Rs. 15,000.00)
Created Current Account: CA2001 for TechCorp (Initial: Rs. 50,000.00)

[Deposit] SB1001 deposited Rs. 5,000.00. New Balance: Rs. 20,000.00
[Withdraw] SB1001 withdrew Rs. 8,000.00. New Balance: Rs. 12,000.00
[Transfer] Transferred Rs. 5,000.00 from SB1001 to CA2001.

Account Statement for SB1001:
- Holder: Aravind
- Type: Savings Account (Min Balance: Rs. 1,000.00)
- Available Balance: Rs. 7,000.00
==================================================
```

## Time and Space Complexity

| Operation | Time Complexity | Space Complexity |
|---|---|---|
| Account Creation | $O(1)$ | $O(1)$ |
| Deposit / Withdrawal | $O(1)$ | $O(1)$ |
| Funds Transfer | $O(1)$ | $O(1)$ |
| Account Lookup | $O(1)$ (Hash Map) | $O(1)$ |
| Total Storage ($N$ accounts) | — | $O(N)$ |

## How to Run

1. Open `Banking_Management_System.ipynb` in Jupyter Notebook or JupyterLab.
2. Select a Python 3 kernel.
3. Run all cells to verify class implementations, polymorphic behaviors, and test scenarios.
