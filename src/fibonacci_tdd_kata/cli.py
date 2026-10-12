"""cli interface for fiibonacci TDD kata."""

import argparse

from fibonacci_tdd_kata import fibonacci


def main() -> None:
    """run fibonacci command-line interface."""
    parser = argparse.ArgumentParser(description="calculate fibonacci number.")
    parser.add_argument(
        "n",
        type=int,
        help="non-negative fibonacci index",
    )
    args = parser.parse_args()

    try:
        result = fibonacci(args.n)
    except ValueError as exc:
        parser.error(str(exc))

    print(result)


if __name__ == "__main__":
    main()
