def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number."""
    a = 0
    b = 1

    for _ in range(n):
        a, b = b, a + b

    return a
