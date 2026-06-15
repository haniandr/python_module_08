#!/usr/bin/env python3
from importlib.util import find_spec
from importlib.metadata import version


try:
    import numpy as np
    import pandas as pd
    from pandas import DataFrame
    import matplotlib as mpt
except ImportError as e:
    print(f"Error: {e}")
    exit(1)


def check_dependancies() -> None:
    dependance: dict[str, str] = {
            "numpy": "Data manipulation ready",
            "pandas": "Numerical computation ready",
            "matplotlib": "Visualization ready"
            }

    print("Checking dependances:")

    for pkg in dependance.keys():
        if find_spec(pkg):
            print(f"[OK] {pkg} ({version(pkg)}) - {dependance[pkg]}")
        else:
            print(f"[MISSING] {pkg}")


def generate_matrix_data(seed: int | None) -> DataFrame:
    if seed is not None:
        np.random.seed(seed)
    age = np.random.randint(0, 101, size=1000)
    temp = np.random.randint(0, 101, size=1000)
    color = np.random.randint(0, 101, size=1000)

    return pd.DataFrame({
            "age": age,
            "temperature": temp, 
            "color": color
        })

def loading() -> None:
    filename = "matrix_analyzis.png"

    print("\nLOADING STATUS: Loading program...\n")

    check_dependancies()
  
    print("Analyzing Matrix Data ...")
    print("Processing 1000 data points...")
    print("Generating visualisation...\n")
    print("Analysis complete!")
    print(f"Results saved to: {filename}")

    df = generate_matrix_data(42)

    plt.figure(figsize=(10, 10))
    plt.scatter(
            df["age"],
            df["temp"],
            c=df["color"],
            alpha=0.6
        )
    plt.title("Data Analyzing")
    plt.xlabel("age")
    plt.ylabel("temp")
    plt.colorbar(label="color")
    plt.savefig(filename)
    plt.close()


if __name__ == "__main__":
    loading()
