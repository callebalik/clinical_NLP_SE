import spacy
from dataMangager.make_neg import make_neg
from dataMangager.make_icd import make_icd
from dataMangager.make_patterns import make_patterns
from typing import Any


def main() -> spacy.language:
    """Main function"""
    nlp = spacy.load(
        "sv_pipeline"
    )  # Load the swedish model (can be done this way since it's installed as a pip package)

    # ToDO Check what function select_pipes(enable="tagger") fills. I think it's just faster as not whole model has to be loaded.

    """ENTITY RULER
    implementation note - Integration with built in named entity recognizer.
    - - -
    Ruler -->  Recognizer =
      - Recognizer respects existing entity spans
      - Adjust its predictions around it.
    Can improve accuracy in some cases.
    - - -
    Recognizer --> Ruler =
      - Ruler only add spans to the doc.ents if they don’t overlap with existing entities predicted by the model
      - To overwrite overlapping entities, you can set overwrite_ents=True on initialization.
    """

    config = {
        "phrase_matcher_attr": "lower",
        "validate": True,  # Whether patterns should be validated (passed to the Matcher and PhraseMatcher). Defaults to False.
        "overwrite_ents": False,
        "ent_id_sep": "||",
    }

    ruler = nlp.add_pipe(
        name="entity_ruler", factory_name="entity_ruler", config=config
    )

    # First we make the patterns
    neg_patterns = make_patterns(phrases=make_neg(), label="NEG")

    icd_lower = [s.lower() for s in make_icd()]

    icd_patterns = make_patterns(phrases=icd_lower, label="SYMFND")

    patterns = neg_patterns + icd_patterns

    # ruler.phrase_matcher = matcher # Changes the phrsematcher
    # ToDO implement test to see that there are no residual patterns
    print("----Printing patterns, should be empty at this point----")
    print(ruler.patterns)
    # with nlp.select_pipes(enable="tagger"):

    ruler.add_patterns(patterns)
    return nlp


# def
# from scripts import app
# import importlib
# from spacy.tokens import DocBin

# nlp = main()


# DOCBIN_PATH = Path(f"{DATA}/processed/corpus/cur")
# doc_bin = DocBin().from_disk(f"{DOCBIN_PATH}/1.spacy")
# doc_bin.merge(DocBin().from_disk(f"{DOCBIN_PATH}/2.spacy"))


# docs = list(doc_bin.get_docs(nlp.vocab))
# # d = doc_bin.get_docs(nlp.vocab)

# docs[0]


if __name__ == "__main__":
    main()
