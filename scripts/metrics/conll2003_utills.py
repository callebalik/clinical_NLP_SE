import pandas as pd
from pandas import DataFrame
from pathlib import Path
import re as re


def conll2003_to_df(file_path) -> DataFrame:
    names = ["TOKEN", "POS", "CHUNK", "NE"]
    df = pd.read_csv(file_path, sep=" ", names=names)
    df.dropna(how="all", inplace=True)  # remove empty lines
    return df


def get_cleaned_label(label: str):
    if "-" in label:
        return label.split("-")[1]
    else:
        return label


def create_target_vector(df: DataFrame):
    return [get_cleaned_label(label) for label in df["NE"]]


def create_total_target_vector(dir_path):
    target_vector = []

    pathlist = Path(dir_path).glob("**/*.conll")

    for path in pathlist:
        target_vector.extend(create_target_vector(conll2003_to_df(path)))
    return target_vector


def create_total_target_df(dir_path):
    pathlist = Path(dir_path).glob("**/*.conll")

    frames = []
    doc = []

    for path in pathlist:
        frame = conll2003_to_df(path)
        doc.append(re.search(r"(\d)(?=.\w+)", path.name).group())
        frames.append(frame)
    return pd.concat(
        frames, keys=doc
    )  # This creates hierarchical index, e.g. a1.loc["3"] all rows for doc 3
