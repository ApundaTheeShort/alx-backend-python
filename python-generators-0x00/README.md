# Python Generators

This project covers Python generators and generator expressions.

## Description

Generators are iterators that produce items one at a time and only when needed.
They are useful for working with large datasets, streaming data, and infinite sequences.

## Learning Objectives

- Create generators using `yield`
- Understand lazy evaluation
- Use generator expressions
- Iterate efficiently over sequences

## Key Concepts

- `yield` pauses a function and returns a value
- The function state is preserved between calls
- Generator expressions provide a compact syntax for creating generators

## Example

```python
def countdown(n):
	while n > 0:
		yield n
		n -= 1

for value in countdown(3):
	print(value)
```

## Usage

Use this project to practice implementing and consuming generators in Python.
