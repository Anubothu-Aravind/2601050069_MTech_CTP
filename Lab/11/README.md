# Object-Oriented Design Patterns — Factory and Strategy

## Objective

Design and implement an extensible e-commerce order billing and payment engine demonstrating the **Factory** and **Strategy** design patterns in Python using Abstract Base Classes (`abc.ABC`), dataclasses, and strict type hinting.

## Problem Statement

An enterprise payment platform must support multiple pricing rules (regular, student discount, seasonal festival promotion) and various payment processing gateways (UPI, Credit Card, NetBanking). The codebase must follow the **SOLID** principles:
- **Open/Closed Principle (OCP)**: New pricing strategies or payment processors should be pluggable without altering existing classes.
- **Single Responsibility Principle (SRP)**: Separating pricing computation, payment authorization, and order context.

## Design Patterns Applied

### 1. Strategy Pattern (`PricingStrategy`)
Enables interchangeable calculation algorithms at runtime:
- `RegularPricing`: Standard 100% price.
- `StudentDiscountPricing`: Applies 20% discount.
- `FestivalOfferPricing`: Applies 35% seasonal concession.

### 2. Factory Pattern (`PaymentProcessorFactory`)
Centralizes object creation and decouples client code from concrete payment classes:
- `UPIPayment`: Instant zero-fee processing.
- `CreditCardPayment`: Adds transaction fee surcharge (1.5%).
- `NetBankingPayment`: Routes through bank gateway.

## Python Program

The implementation is located in:

`Design_Patterns_Factory_Strategy.ipynb`

### Sample Output

```text
Order: ORD101 | Final: Rs. 800.00 | Status: Paid Rs. 800.00 instantly via UPI (Zero surcharge)
Order: ORD102 | Final: Rs. 3250.00 | Status: Paid Rs. 3298.75 via Credit Card (includes 1.5% gateway fee)
```

## UML / Pattern Architecture

```text
                  +---------------------------+
                  |  <<interface>> Strategy   |
                  |     PricingStrategy       |
                  +---------------------------+
                                ^
               +----------------+----------------+
               |                                 |
    +-----------------------+         +-----------------------+
    | StudentDiscountPricing|         | FestivalOfferPricing  |
    +-----------------------+         +-----------------------+

                  +---------------------------+
                  |    PaymentProcessorFactory|
                  +---------------------------+
                                | creates
                                v
                  +---------------------------+
                  | <<interface>> Processor   |
                  |     PaymentProcessor      |
                  +---------------------------+
                                ^
               +----------------+----------------+
               |                                 |
    +-----------------------+         +-----------------------+
    |      UPIPayment       |         |   CreditCardPayment   |
    +-----------------------+         +-----------------------+
```

## Complexity Analysis

- **Time Complexity**:
  - Factory Instantiation: $O(1)$ dictionary lookup.
  - Strategy Execution: $O(1)$ computation.
- **Space Complexity**: $O(1)$ auxiliary memory overhead per transaction.

## How to Run

1. Open `Design_Patterns_Factory_Strategy.ipynb` in Jupyter Notebook.
2. Select Python 3 kernel.
3. Run all cells to verify dynamic polymorphism and runtime strategy switching.
