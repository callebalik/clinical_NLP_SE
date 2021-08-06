"""
Gets all files of conll format (change dir depending on source) and renames them to their parent div, instead of annotator name.

One could extend the name to retain this info.

Summary of actions in table s
"""
import glob
from pathlib import Path
from tabulate import tabulate
import pandas as pd
import shutil

file_path = Path(__file__).resolve()

SRC_PATH = file_path.parent.parent
DATA_PATH = SRC_PATH.parent / "data"


def move_conll_files(glob):
    all_files = []

    for file in glob:

        if file.name == "admin.conll":
            continue
        else:
            new_name = f"{file.parent.stem}_{file.name}"
            # new_name = name.__add__(".conll")
            new_path = file.parent.parent / new_name
            all_files.append((file.name, file.parent, new_name, new_path))
            to_file = DATA_PATH / "interim/corpus/" / new_name
            shutil.copy2(file, str(to_file))
    columns = ["File_Name", "Parent", "new_name", "copied to"]
    df = pd.DataFrame.from_records(all_files, columns=columns)
    print(tabulate(df, headers=columns, tablefmt="psql"))


ANNOTATION_PATH = DATA_PATH / "raw/corpus/annotation"
CURATION_PATH = DATA_PATH / "raw/corpus/curation"

move_conll_files(ANNOTATION_PATH.glob("*/*.conll"))
move_conll_files(CURATION_PATH.glob("*/*.conll"))


def rename_inception_files():
