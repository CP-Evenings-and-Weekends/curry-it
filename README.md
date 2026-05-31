# Curry It

## What is Currying?

Currying transforms a function that takes multiple arguments into a chain of functions that each take a single argument.

```python
# Before:  add(1, 2, 3)
# After:   add(1)(2)(3)
```

## Requirements

Write a function called `curry` (Python) / `curry` (JS) that takes any function and returns a curried version of it.

- The curried version should accept arguments one at a time.
- Once all required arguments have been provided, the original function should run with those arguments and return its result.
- Your `curry` should work with functions of any arity (2, 3, 4+ args).

## Examples

```python
def add(a, b, c):
    return a + b + c

curried_add = curry(add)
curried_add(1)(2)(3)     # -> 6
curried_add(10)(20)(30)  # -> 60
```

```javascript
const multiply = (a, b, c) => a * b * c;
const curriedMultiply = curry(multiply);
curriedMultiply(2)(3)(4);  // -> 24
```

## Test Your Code

- Python: `python curry_tests.py`
- JS: `node curryTests.js`

## Stretch

Make your curry function support partial application: `curried_add(1, 2)(3)` and `curried_add(1)(2, 3)` should both work.
