import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _(mo):


    mo.md("""
    #fibonacci tdd kata
    here I have implemented fibonacci seq using tdd.

    the process is as:
    green-> red ->refactor
    """)
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    #version1
    # def fibonacci(n):
    #     if n == 0:
    #         return 0
    #     if n == 1:
    #         return 1
    #     return fibonacci(n-1) + fibonacci(n-2)
    return


@app.cell
def _(mo):
    user_input=mo.ui.number(
        start=0,
        step=1,
        value=10,
        label="n"
    )
    user_input
    return (user_input,)


@app.function
#reactored version
def fibonacci(n):
     a=0
     b=1
     for _ in range(n):
         a,b=b, a+b
     return a


@app.cell
def _(mo, user_input):
    result=fibonacci(user_input.value)
    mo.md(
        f"**F({user_input.value}) = {result}**"
    )
    return


@app.function
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5


if __name__ == "__main__":
    app.run()
