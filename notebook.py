import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.function
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


@app.function
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
