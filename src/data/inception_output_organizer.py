'''
Gets all files of conll format (change dir depending on source) and renames them to their parent div, instead of annotator name.

One could extend the name to retain this info.

Summary of actions in table s
'''
import glob
from pathlib import Path
from tabulate import tabulate
import pandas as pd
import shutil

file_path = Path(__file__).resolve()

SRC_PATH = file_path.parent.parent
DATA_PATH = SRC_PATH.parent / 'data'

conll_path = DATA_PATH / 'raw/conll2003/'

all_files = []

for file in conll_path.glob('*/*.conll'):

    name = (file.parent.stem)
    new_name = name.__add__('.conll')
    new_path = file.parent.parent / new_name
    all_files.append((file.name, file.parent, new_name, new_path))
    to_file = conll_path / new_name
    shutil.copy2(file, str(to_file))


columns = ["File_Name", "Parent", "new_name", "copied to"]
df = pd.DataFrame.from_records(all_files, columns=columns)

print(tabulate(df, headers = columns, tablefmt='psql'))