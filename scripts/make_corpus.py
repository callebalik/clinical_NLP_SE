from pathlib import Path
import os
import subprocess

# ToDo Make this step work as native python code instead of shell shifting colab adjustment
# ToDo SEtup test to check that conversion works after INCEpTION export problem is


file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent
print(ROOT)
DATA_PATH = ROOT / "data"
NEG_PATH = DATA_PATH / "raw/negations"

corpus_name = "conll2003_NE_built_in_layer"

RAW_CORPUS_PATH = DATA_PATH / f"raw/corpus/{corpus_name}"
OUTPUT_CORPUS_PATH = DATA_PATH / f"processed/corpus/{corpus_name}"

# convert the annotated corpus to spacy example format
# use 100 sentences before splitting a file into a new doc
# /home/callebalik/clinical_NLP_SE/data/processed/corpus/conll2003_NE_built_in_layer
# /home/callebalik/clinical_NLP_SE/scripts/data/processed/corpus/conll2003_NE_built_in_layer/
def convert_raw_to_spacy():

    # cmd = "
    #     "python",
    #     "-m",
    #     "spacy",
    #     "convert",
    #     {RAW_CORPUS_PATH},
    #     {OUTPUT_CORPUS_PATH},
    #     "--converter",
    #     "conll",
    #     "--n-sents",
    #     "100",
    # "
    cmd = f"python -m spacy convert {RAW_CORPUS_PATH}/ {OUTPUT_CORPUS_PATH}/ --converter conll --n-sents 100"
    print(cmd)
    output = subprocess.run(f"{cmd}", capture_output=True)
    print(output)


def main():
    convert_raw_to_spacy()


if __name__ == "__main__":
    main()
