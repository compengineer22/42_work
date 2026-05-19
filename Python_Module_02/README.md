# Garden Guardian

> Data Engineering for Smart Agriculture

A Python project from the 42 Beirut curriculum focused on exception handling, defensive programming, and resilient data pipelines for smart agriculture systems.

## About

This project introduces the fundamentals of Python exception handling through agricultural monitoring scenarios.
The goal is to build fault-tolerant programs capable of handling invalid sensor data, runtime failures, custom exceptions, and resource cleanup without crashing.

Throughout the exercises, the project explores:

* Input validation
* Exception handling with `try` / `except`
* Raising custom exceptions
* Managing multiple error types
* Using `finally` for cleanup
* Writing resilient and readable Python code

---

## Project Structure

```bash
.
├── ex0/
│   └── ft_first_exception.py
├── ex1/
│   └── ft_raise_exception.py
├── ex2/
│   └── ft_different_errors.py
├── ex3/
│   └── ft_custom_errors.py
└── ex4/
    └── ft_finally_block.py
```

---

## Exercises

### Exercise 00 — Agricultural Data Validation

Introduction to basic exception handling.

Topics covered:

* Converting user input
* Handling invalid values
* Preventing program crashes

---

### Exercise 01 — Agricultural Data Validation Pipeline

Improved validation with custom checks.

Topics covered:

* Raising exceptions manually
* Range validation
* Defensive programming

---

### Exercise 02 — Different Types of Problems

Working with multiple built-in exceptions.

Topics covered:

* `ValueError`
* `ZeroDivisionError`
* `FileNotFoundError`
* `TypeError`
* Catching multiple exceptions

---

### Exercise 03 — Making Your Own Error Types

Creating custom exception classes.

Topics covered:

* Inheritance
* Custom error messages
* Organizing application-specific errors

---

### Exercise 04 — Finally Block

Ensuring cleanup even after failures.

Topics covered:

* `finally`
* Resource cleanup
* Error-safe program flow

---

## Requirements

* Python 3.10+
* flake8
* mypy

---

## Usage

Run each exercise individually:

```bash
python3 ex0/ft_first_exception.py
python3 ex1/ft_raise_exception.py
python3 ex2/ft_different_errors.py
python3 ex3/ft_custom_errors.py
python3 ex4/ft_finally_block.py
```

---

## Code Rules

This project follows the subject requirements:

* Python 3.10+
* Type hints required
* flake8 compliant
* Clear and readable code
* Programs must never crash
* Proper use of exception handling

---

## Learning Objectives

By completing this project, you will understand:

* How Python exceptions work
* How to handle runtime errors safely
* When to raise exceptions
* How to create custom exception types
* How to write more reliable applications

---

## Author:

hsrour