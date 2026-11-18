"""Clean raw events: drop bad rows and normalize timestamps."""

from pathlib import Path

import pandas as pd

VALID_EVENT_TYPES = {"click", "login", "purchase", "scroll", "view"}

RAW_PATH = Path("data/raw/events.csv")
OUT_PATH = Path("data/clean/events.csv")


def main() -> None:
    df = pd.read_csv(RAW_PATH)

    # Drop rows with any missing fields
    df = df.dropna(how="any")
    df = df[df["user_id"].astype(str).str.strip() != ""]
    df = df[df["timestamp"].astype(str).str.strip() != ""]
    df = df[df["event_type"].astype(str).str.strip() != ""]
    df = df[df["duration_seconds"].astype(str).str.strip() != ""]

    # Keep only valid event types
    df = df[df["event_type"].isin(VALID_EVENT_TYPES)]

    # Non-positive durations out; keep whole numbers
    df["duration_seconds"] = pd.to_numeric(df["duration_seconds"], errors="coerce")
    df = df.dropna(subset=["duration_seconds"])
    df = df[df["duration_seconds"] > 0]
    df["duration_seconds"] = df["duration_seconds"].astype(int)

    # Normalize timestamps to YYYY-MM-DDTHH:MM:SS
    df["timestamp"] = pd.to_datetime(df["timestamp"], format="mixed")
    df = df.dropna(subset=["timestamp"])
    df["timestamp"] = df["timestamp"].dt.strftime("%Y-%m-%dT%H:%M:%S")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)


if __name__ == "__main__":
    main()
