import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.function
def fibonacci(n):
    pass


@app.cell
def _():
    # def test_fibonacci(n):
    #     assert fibonacci(0) == 0
    #     assert fibonacci(1) == 1
    #     assert fibonacci(2) == 2
    #     assert fibonacci(3) == 3
    #     assert fibonacci(4) == 4
    #     assert fibonacci(5) == 5
    return


@app.cell
def _():
    # def test_fibonacci_zero():
    #     assert fibonacci(0) == 0

    # def test_fibonacci_one():
    #     assert fibonacci(1) == 1

    # def test_fibonacci_sequence():
    #     assert fibonacci(2) == 1
    #     assert fibonacci(3) == 2
    #     assert fibonacci(4) == 3
    #     assert fibonacci(5) == 5
    return


if __name__ == "__main__":
    app.run()
