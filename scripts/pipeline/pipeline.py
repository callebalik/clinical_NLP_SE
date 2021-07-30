import spacy
import re
from typing import List

def main() -> None:
    """ Main function """
    nlp = spacy.load("sv_pipeline") # Load the swedish model (can be done this way since it's installed as a pip package)

if __name__ == '__main__':
    main()


def get_icd() -> List :
    """ Processing ICD codes using regex"""


    # pattern and special signs
    # LDD   LLLLLL
    # LDD † LLLLLL
    # LDD * LLLLLL

    # Example
    # P75	*	Mekoniumileus vid cystisk fibros (E84.1)

    """
    Positive Lookbehind (?<=\D\d\d) Assert that the Regex below matches
    \D matches any character that's not a digit (equivalent to [^0-9])
    \d matches a digit (equivalent to [0-9])
    \d matches a digit (equivalent to [0-9])
    \s matches any whitespace character (equivalent to [\r\n\t\f\v ])
    +? matches the previous token between one and unlimited times, as few times as possible, expanding as needed (lazy)
    . matches any character (except for line terminators)
    ? matches the previous token between zero and one times, as many times as possible, giving back as needed (greedy)
    \s matches any whitespace character (equivalent to [\r\n\t\f\v ])
    """

    # Global pattern flags
    # g modifier: global. All matches (don't return after first match)
    # m modifier: multi line. Causes ^ and $ to match the begin/end of each line (not only begin/end of string)

    regex_ddd = '/(?<=\D\d\d)\s+?.?\s/gm'
    regex_dddR = '/(?<=R\d\d)\s+?.?\s/gm'
    ddd = r'(?<=\D\d\d)\s+?.?\s'
    dddd = r'(?<=\D\d\d\d)\s+?.?\s'
    ddddd = r'((?<=\D\d\d\d\d)|(?<=\D\d\d\d\D))\s+?.?\s'

    '''
    A513B	†	Syfilitisk (sekundär) alopeci (L99.8)
    Y3498		Ospecificerad skadehändelse, med oklar avsikt-plats, ospecificerad-andra specificerade aktiviteter
    Y3499		Ospecificerad skadehändelse, med oklar avsikt-plats, ospecificerad-aktivitet, ospecificerad
    Y586A		Komplikation av vaccin mot kikhosta, enbart (P)
    Y586B		Komplikation av vaccin mot difteri, kikhosta och stelkramp, kombinerat (DPT)
    Y586W		Komplikation av annat kombinerat
    '''

    ICD_PATH = data_path / 'raw/codes/icd-10-se-2021-text'
    file_path = ICD_PATH / 'digit3.txt'

    ICD000 = []
    with open(ICD_PATH / 'digit3.txt','r') as codes:
        for line in codes:
            x = re.split(ddd, line)
            ICD000.append(x[1].strip())

    ICD0000 = []
    with open(ICD_PATH / 'digit4.txt','r') as codes:
        for line in codes:
            x = re.split(dddd, line)
            ICD0000.append(x[1].strip())

    ICD00000 = []
    with open(ICD_PATH / 'digit5.txt','r') as codes:
        for line in codes:
            x = re.split(ddddd, line)
            ICD00000.append(x[1])

    ICD = ICD000 + ICD0000 + ICD00000

    return ICD