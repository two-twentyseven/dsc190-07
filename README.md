# dsc190-07

DSC 190 Assignment 07: reproducible data pipeline with DVC and Marimo.

## Setup

```bash
uv sync
```

## Reproduce the pipeline

```bash
uv run dvc repro
```

This regenerates:

- `data/clean/events.csv`
- `data/transformed/events.csv`
- `data/features/events.csv`

## Notebook

```bash
uv run marimo edit notebooks/report.py
```
