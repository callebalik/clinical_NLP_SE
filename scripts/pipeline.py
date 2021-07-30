"""
create spacy pipeline
"""

from typing import List
import spacy

def make_patterns(patterns:List, label:str, nlp:spacy.language) -> :
    patterns = [nlp.make_doc(p.lower()) for p in patterns]

    patterns = []

    for pattern in icd_entries:
        p = {"label":"SYM","pattern":[{"LOWER":str(pattern)}]} # adds rule to label lowercase str of icd_code
    patterns.append(p)

    for pattern in neg_phrases:
        p = {"label":"NEG","pattern":[{"LOWER":str(pattern)}]}
    patterns.append(p)

def create_entity_ruler(nlp:spacy.language):

    # ENTITY RULER

    # implementation note - Integration with built in named entity recognizer.
    # - - -
    # Ruler -->  Recognizer =
    #   - Recognizer respects existing entity spans
    #   - Adjust its predictions around it.
    # Can improve accuracy in some cases.
    # - - -
    # Recognizer --> Ruler =
    #   - Ruler only add spans to the doc.ents if they don’t overlap with existing entities predicted by the model
    #   - To overwrite overlapping entities, you can set overwrite_ents=True on initialization.

    config = {
        "phrase_matcher_attr": "lower",
        "validate": True, # Whether patterns should be validated (passed to the Matcher and PhraseMatcher). Defaults to False.
        "overwrite_ents": False,
        "ent_id_sep": "||",
        }

    ruler = nlp.replace_pipe(name="entity_ruler", factory_name="entity_ruler", config=config)

    #ruler.phrase_matcher = matcher # Changes the phrsematcher
    # ToDO implement test to see that there are no residual patterns
    print("----Printing patterns, should be empty at this point----")
    print(ruler.patterns)

    # Add patterns to the entity ruler



    # ToDO Check what function select_pipes(enable="tagger") fills. I think it's just faster as not whole model has to be loaded.
    with nlp.select_pipes(enable="tagger"):
        ruler.add_patterns(patterns)


    # nlp.pipeline # pipeline components
    # ruler.patterns # ruler patterns

    # --------
    # save ruler to disk in jsonl format - can then be loaded to model
    #ruler.to_disk(Path(repo_path / "models/patterns.jsonl"))

