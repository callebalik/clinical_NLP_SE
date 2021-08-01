# Evaluate model
import os
from pathlib import Path

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent

model_name = "test"


def save_model(nlp):
    nlp.to_disk(ROOT / f"models/{model_name}/")  # save model to disk
