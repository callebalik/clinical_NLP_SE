from tabulate import tabulate
import pandas as pd
import spacy

"""
    raw text
    lemma – a root form of the word
    part of speech
    a flag for whether the word is a stopword – i.e., a common word that may be filtered out
"""


def spacy_tabulate(doc) -> None:
    cols = ("NE", "IOB", "text", "lemma", "POS", "dep", "right edge")

    df = pd.DataFrame()

    rows = []

    for t in doc:
        if t.ent_type_ == "SYM" or "NEG":
            row = [
                t.ent_type_,
                t.ent_iob_,
                t.text,
                t.lemma_,
                spacy.explain(t.pos_),
                t.dep_,
                t.right_edge,
            ]

            rows.append(row)

    df = pd.DataFrame(rows, columns=cols)
    print(tabulate(df, headers=cols, tablefmt="psql", showindex=False))
