# TODO: point to your Model
import spacy
from spacy.training import offsets_to_biluo_tags


def create_total_prediction_vector(nlp: spacy.language, docs: list):
    prediction_vector = []
    for doc in docs:
        prediction_vector.extend(create_prediction_vector(nlp, docs))
    return prediction_vector


def create_prediction_vector(nlp: spacy.language, text):
    return [
        get_cleaned_label(prediction)
        for prediction in get_all_ner_predictions(nlp, text)
    ]


def get_cleaned_label(label: str):
    if "-" in label:
        return label.split("-")[1]
    else:
        return label


def get_all_ner_predictions(nlp: spacy.language, text):
    doc = nlp(text)
    entities = [(e.start_char, e.end_char, e.label_) for e in doc.ents]
    bilou_entities = offsets_to_biluo_tags(doc, entities)
    return bilou_entities
