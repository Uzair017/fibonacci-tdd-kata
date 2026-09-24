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


@app.cell
def fibonacci():
    #refactored version
    # def fibonacci(n):
    #      a=0
    #      b=1
    #      for _ in range(n):
    #          a,b=b, a+b
    #      return a
    return


@app.function
#latest optimized version which also handles large values
def fibonacci(n):
    if n<0:
        raise ValueError("n must not be negative")
    def fast_doubling_algo(k):
        if k ==0:
            return 0,1
        a,b=fast_doubling_algo(k//2)
        c= a*(2*b-a)
        d=a*a+b*b

        if k%2==0:
            return c,d
        return d,c+d
    return fast_doubling_algo(n)[0]


@app.cell
def _(mo, user_input):
    result=fibonacci(user_input.value)
    mo.md(
        f"**F({user_input.value}) = {result}**"
    )
    return


@app.function
def test_10M_number_fibonacci():
    result= fibonacci(10_000_000)
    assert result>0


@app.function
def test_fibonacci():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5


@app.function
#additional test for big values
def test_largenumbers_fibonacci():
    assert fibonacci(10) == 55
    assert fibonacci(100) == 354224848179261915075


if __name__ == "__main__":
    app.run()
