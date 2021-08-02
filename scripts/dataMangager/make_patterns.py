""" Make patterns """

from typing import List


def make_patterns(phrases: List, label: str, id=None) -> list:
    # patterns = [nlp.make_doc(p.lower()) for p in patterns]

    patterns = []

    for pattern in phrases:
        if id != None:
            p = {
                "label": label,
                "pattern": [{"LOWER": pattern}],
                "id": "id",
            }  # adds rule to label lowercase str of icd_code
            patterns.append(p)
        else:
            p = {
                "label": label,
                "pattern": [{"LOWER": pattern}],
            }  # adds rule to label lowercase str of icd_code
            patterns.append(p)

    return patterns
