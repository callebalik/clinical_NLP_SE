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
import re as re
import os

file_path = Path(__file__).resolve()

SRC_PATH = file_path.parent.parent
DATA_PATH = SRC_PATH.parent / "data"


def move_conll_files(glob):
    all_files = []

    for file in glob:

        if file.name == "admin.conll":
            continue
        else:
            record = file.parent.stem
            a = re.search(r"(\d)", record)
            print(a.group())
            doc_nr = (
                re.search(r"(\d)", file.parent.stem).group()
                if re.search(r"(chart)", file.parent.stem)
                else (int(re.search(r"(\d)", file.parent.stem).group()) + 5)
            )

            if re.search(r"annotator1", file.name):
                annotator = "a1"
            elif re.search(r"Annotator", file.name):
                annotator = "a2"
            elif re.search(r"CURATION", file.name):
                annotator = "cur"
            else:
                raise ValueError

            new_name = f"{annotator}/{doc_nr}.conll"

            # new_name = name.__add__(".conll")
            new_path = f"{DATA_PATH / f'interim/corpus/' / new_name}"
            all_files.append((file.name, file.parent, new_name, new_path))
            to_file = DATA_PATH / f"interim/corpus/" / new_name
            os.makedirs(os.path.dirname(to_file), exist_ok=True)
            shutil.copy2(file, str(to_file))
    columns = ["File_Name", "Parent", "new_name", "copied to"]
    df = pd.DataFrame.from_records(all_files, columns=columns)
    print(tabulate(df, headers=columns, tablefmt="psql"))


ANNOTATION_PATH = DATA_PATH / "raw/corpus/annotation"
CURATION_PATH = DATA_PATH / "raw/corpus/curation"

move_conll_files(ANNOTATION_PATH.glob("*/*.conll"))
move_conll_files(CURATION_PATH.glob("*/*.conll"))


# def rename_inception_files():
