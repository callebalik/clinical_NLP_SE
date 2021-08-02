# Evaluate model
import os
from pathlib import Path
import subprocess

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent
DATA_PATH = ROOT / "data"

corpus_name = "conll2003_NE_built_in_layer"
RAW_CORPUS_PATH = DATA_PATH / f"raw/corpus/{corpus_name}"
OUTPUT_CORPUS_PATH = DATA_PATH / f"processed/corpus/{corpus_name}"


def save_model(nlp, model_name: str):
    nlp.to_disk(ROOT / f"models/{model_name}/")  # save model to disk
    print(f"model saved as {model_name}")


# convert the annotated corpus to spacy example format
# use 100 sentences before splitting a file into a new doc
# /home/callebalik/clinical_NLP_SE/data/processed/corpus/conll2003_NE_built_in_layer
# /home/callebalik/clinical_NLP_SE/scripts/data/processed/corpus/conll2003_NE_built_in_layer/


def evaluate_model(model_name: str):
    MODEL_PATH = ROOT / f"models/{model_name}"
    output = f"--output {MODEL_PATH}/metrics.json"
    displacy = f"--displacy-path {MODEL_PATH}"

    cmd = (
        f"python -m spacy evaluate"
        + " "
        + f"{MODEL_PATH} {OUTPUT_CORPUS_PATH}"
        + " "
        + output
        + " "
        + displacy
    )
    output = subprocess.call(f"{cmd}", shell=True)
    print(output)
