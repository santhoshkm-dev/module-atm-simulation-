# module-atm-simulation-
A Python-based terminal ATM application built using Object-Oriented Programming (OOP) and structural module separation, featuring custom authentication and dynamic OTP verification.
# Modular ATM Simulation System

A terminal-based ATM application written in Python that simulates core banking workflows. The project emphasizes clean code practices, strict separation of concerns, and Object-Oriented Programming (OOP) principles. 

Instead of dumping all logic into a single monolithic file, this system uses independent modules interacting with each other to manage state and application flow.

## 🚀 Key Features

- **Decoupled Architecture:** Separate modules for Login, Balance Management, and Withdrawals.
- **State Interaction:** The Withdrawal module dynamically interacts with the balance state across classes.
- **Secure Authentication:** Multi-attempt login protection with error-safe handling.
- **OTP Verification Module:** 6-digit random verification code generator with active countdown retries and basic phone number validation.
- **Robust Exception Handling:** Full validation against edge cases like `ValueError` for inputs and `ZeroDivisionError` prevention in math workflows.

## 📂 Project Structure

```text
modular-atm-system/
│
├── main.py            # Application controller & system workflow runner
├── login.py           # Verification logic & credential handling class
├── balance.py         # Account state management (Check/Deposit)
└── withdrawal.py      # Transaction processor (interacts with Balance state)

Author:
santhosh km
