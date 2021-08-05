"""
Evaluate IAA for INCEpTION output
"""

from pathlib import Path
from typing import Any, Dict, Type
import re as re
import pandas as pd

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent.parent
DATA_PATH = ROOT / "data"
AGREEMENT_PATH = DATA_PATH / "raw/coprus/agreement.csv.txt"

from pathlib import path


with open(
    DATA_PATH / "raw/coprus/agreement.csv.txt", mode="r", encoding="utf-8-sig"
) as blocks:  # Giving the correct encoding, the BOM is omitted in the result: \ufefftest'
    for block in blocks:
        block = re.split(r"$\s", block)  # remove trailing whitespace
        block = re.split(r"(?<=\w\d\d)\s+", block[0])  # split block codes from text

        # Set start end and text in a list as values for the corresponing key
        self.blocks[block[0]] = {"text": block[1]}


data = pd.read_csv(AGREEMENT_PATH)

print(data.head())
