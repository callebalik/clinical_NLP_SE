from pathlib import Path
import os
import subprocess

# ToDo Make this step work as native python code instead of shell shifting colab adjustment
# ToDo SEtup test to check that conversion works after INCEpTION export problem is


file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent
print(ROOT)
DATA_PATH = ROOT / "data"

corpus_name = "conll2003_NE_built_in_layer"
RAW_CORPUS_PATH = DATA_PATH / f"raw/corpus/{corpus_name}"
OUTPUT_CORPUS_PATH = DATA_PATH / f"processed/corpus/{corpus_name}"

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
        + f"{MODEL_PATH} {OUTPUT_CORPUS_PATH}"
        + output
        + displacy
    )
    output = subprocess.call(f"{cmd}", shell=True)
    print(output)
