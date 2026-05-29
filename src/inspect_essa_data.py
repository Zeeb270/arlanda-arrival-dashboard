from pathlib import Path
import pandas as pd

DATA_DIR = Path("data/raw/ESSA")

files = [
    "ESSA_stats.csv",
    "ESSA_TEST_X.tsv",
    "ESSA_TEST_Y.tsv",
    "ESSA_TEST_Z.tsv",
]

print("\n==============================")
print("ESSA DATASET INSPECTION")
print("==============================")

print("\n1) FILE CHECK")
for file in files:
    path = DATA_DIR / file
    if path.exists():
        size_mb = path.stat().st_size / 1024 / 1024
        print(f"OK  {file:18s}  {size_mb:8.2f} MB")
    else:
        print(f"NO  {file:18s}  MISSING")

print("\n2) STATS FILE")
stats_path = DATA_DIR / "ESSA_stats.csv"
if stats_path.exists():
    stats = pd.read_csv(stats_path)
    print("Shape:", stats.shape)
    print("Columns:", list(stats.columns))
    print(stats)

print("\n3) MATRIX FILE SUMMARIES")

for file in ["ESSA_TEST_X.tsv", "ESSA_TEST_Y.tsv", "ESSA_TEST_Z.tsv"]:
    path = DATA_DIR / file
    print("\n------------------------------")
    print(file)
    print("------------------------------")

    if not path.exists():
        print("Missing file")
        continue

    # Count lines without loading entire file
    with open(path, "r") as f:
        n_lines = sum(1 for _ in f)

    print("Number of rows:", n_lines)

    # Read a small sample only
    sample = pd.read_csv(path, sep="\t", header=None, nrows=5)

    print("Sample shape:", sample.shape)
    print("Number of columns:", sample.shape[1])

    print("\nFirst 10 values of first row:")
    print(sample.iloc[0, :10].tolist())

    print("\nNon-null values per sample row:")
    print(sample.notna().sum(axis=1).tolist())

    print("\nFirst 5 rows, first 8 columns:")
    print(sample.iloc[:, :8])
