import pandas as pd
import re
import csv
from pathlib import Path
from inspect import getsourcefile
from os.path import abspath

# get file path, should work on most systems
#file_path = abspath(getsourcefile(lambda:0))

file_path = Path(__file__).resolve()

SRC_PATH = file_path.parent.parent
DATA_PATH = SRC_PATH.parent / 'data'


neg_terms = {}

with open(DATA_PATH / 'raw/negations/negEx.txt','r', encoding='utf-8') as negations:
    for line in negations:
        x = line.split("\t")
        key = x[0]
        value = x[1].strip()
        value = value.rstrip("]")
        value = value.lstrip("[")
        neg_terms[key] = value


print(neg_terms)
df = pd.DataFrame.from_dict(neg_terms, orient="index")

print(df)
df.sort_index().to_csv(DATA_PATH / 'interim/negEx_sorted.csv', encoding="utf-8")