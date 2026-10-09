import marimo

__generated_with = "0.24.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    mo.md("""
    # Fibonacci explorer
     explore fibonacci seq interactively.
     choose a maximum index to see the numbers n their distributions.""")
    return (mo,)


@app.cell
def _(mo):
    # slider
    max_num = mo.ui.slider(start=0, stop=20, value=10, label="Max fibonacci index")
    max_num
    return (max_num,)


@app.cell
def _(max_num):
    # calculatings vals from package
    from fibonacci_tdd_kata import fibonacci

    indices = list(range(max_num.value + 1))
    results = [fibonacci(n) for n in indices]
    return indices, results


@app.cell
def _(indices, results):
    # chart
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.bar(indices, results)
    ax.set_title("fibonacci seq")
    ax.set_xlabel("index")
    ax.set_ylabel("fibonacci num")
    ax.set_xticks(indices)
    fig.tight_layout()
    fig
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
