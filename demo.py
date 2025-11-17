# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair==6.0.0",
#     "polars==1.35.2",
# ]
# ///

import marimo

__generated_with = "0.17.8"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    return mo, pl


@app.cell
def _(mo):
    x_slider = mo.ui.slider(0, 100, 1, value=50)
    x_slider
    return (x_slider,)


@app.cell
def _(pl, x_slider):
    pl.DataFrame({
        "x": [i for i in range(x_slider.value)],
        "y": [i**2 for i in range(x_slider.value)]
    }).plot.line(x="x", y="y")
    return


if __name__ == "__main__":
    app.run()
