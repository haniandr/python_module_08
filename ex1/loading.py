#!/usr/bin/env python3
from importlib.util import find_spec
from importlib.metadata import version


try:
    import numpy as np
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

    for pkg in dependance.keys():
        if find_spec(pkg):
            print(f"[OK] {pkg} ({version(pkg)}) - {dependance[pkg]}")
        else:
            print(f"[MISSING] {pkg}")


def generate_matrix_data() 
