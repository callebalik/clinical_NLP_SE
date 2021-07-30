import spacy
from scripts.pipeline import make_patterns

def main() -> None:
    """ Main function """
    nlp = spacy.load("sv_pipeline") # Load the swedish model (can be done this way since it's installed as a pip package)

    make_patterns(nlp)



if __name__ == '__main__':
    main()
