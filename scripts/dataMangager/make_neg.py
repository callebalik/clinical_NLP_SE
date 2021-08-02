""" Processing negations """


from pathlib import Path
import re
from typing import List

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent.parent
DATA_PATH = ROOT / "data"
NEG_PATH = DATA_PATH / "raw/negations"


def make_neg() -> List:
    negations = {}
    with open(NEG_PATH / "negEx2.txt", "r") as neg:
        for line in neg:
            x = re.split(r"\s+(?=\[)", line)
            n = [x[0].strip(), x[1].strip()]
            negations[x[0]] = x[1].strip()
    return negations
