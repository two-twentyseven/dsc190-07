import marimo

__generated_with = "0.25.2"
app = marimo.App()


@app.cell
def _():
    import marimo as mo
    import pandas as pd
    import matplotlib.pyplot as plt
    return mo, pd, plt


@app.cell
def _(mo):
    mo.md("""# Event Duration Report

    Histogram of `duration_minutes` from the DVC features stage.
    """)
    return


@app.cell
def _(pd):
    df = pd.read_csv("data/features/events.csv")
    df
    return (df,)


@app.cell
def _(df, plt):
    fig, ax = plt.subplots()
    ax.hist(df["duration_minutes"], bins=30, edgecolor="black")
    ax.set_xlabel("duration_minutes")
    ax.set_ylabel("count")
    ax.set_title("Distribution of event durations")
    fig
    return


if __name__ == "__main__":
    app.run()
