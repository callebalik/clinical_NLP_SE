# module that takes raw icd10 codes and returns a dictionary with categories

from pathlib import Path
from typing import Dict, TypedDict
import re

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent
DATA_PATH = ROOT / 'data'
ICD_PATH = DATA_PATH / 'raw/medical_codes/icd-10-se-2021-text'


    # Chapter <-> description
    #       blocks 2 numbers
    #           3 digit
    #               4 digit
    #                   5 digit
    # We want to be able to pass the code e.g. B995 and return the value
    # we also want to be able to get all codes in a certain range and specificity
    # -----
    # As this is somewhat hard to model intuitively and since we want to be able to resuse and extend as well a manipulate the data, a class to handle this seems appropriate

# class IcdDict(TypedDict):
#     code:str
#     text:str

# ToDo these would probably do better as class representations
class Icd:

    codes: Dict

    def __init__(self):
        # IcdDict self.codes = TypedDict('Icd', {'key': str, 'value': str})
        self.codes = {}
        self.make_block()

    def __repr__(self) -> str:

        pass
    # !issue: get \ufeffA00 for first code, both in block and digit3 file

    def make_block(self) -> None:
        with open(ICD_PATH / 'block.txt','r') as codes:
            for row in codes:
                row = re.split(r'$\s',row) # remove trailing whitespace
                row = re.split(r'(?<=\w\d\d)\s+', row[0]) # split codes from text
                index = row[0]
                index_start_end = re.split(r'(?<=\d)-(?=\D)', index) # split start end end of code at - e.g. A30-A49
                index_start_end = re.split(r'(?<=\d)-(?=\D)', index) # split start end end of code at - e.g. A30-A49

                # Set start end and text in a list as values for the corresponing key
                list = [index_start_end[0], index_start_end[1], row[1]]
                # Set start end and text in a list as values for the corresponing key
                list = [index_start_end[0], index_start_end[1], row[1]]
                self.codes[index] = list

    def make_tree_dig(self) -> Dict:
        dict_three = {}

        with open(ICD_PATH / 'digit3.txt','r') as codes:
            for r in codes:
                r = re.split(r'$\s',r)
                # special cases -- add info
                row = re.split(r'(?<=\w\d\d)\s+', r[0])
                dict_three[row[0]] = row[1]
            return dict_three

    def get_chapter_start(self, chapter:str) -> str:
        return self.codes[chapter][0]

    def get_chapter_end(self, chapter:str) -> str:
        return self.codes[chapter][1]

    def get_chapter(self, index:str) -> str:
        """ Matches a given code index e.g. B07 to it's correct chapter parent and returns the key for the chapter as a str """

        for key in self.codes:
            if self.get_chapter_end(key) >= index:   # compare chapter end to index, if index < end, then it's in that chapter
            # error if we reach end of list without matching, but shouldn't happen in this contained example.
                return key

    def get_chap_text(self, index=str) -> str:
        """ Get the text for the chapter of a given index """
        level = len(index) - 1 # Gets the number of numbers in the index

        chap_key = self.get_chapter(index=index)
        return self.codes[chap_key][2] # chapter text

    def get_text(self, index=str) -> str:
        """ Get the text for the specific index """
        level = len(index) - 1 # Gets the number of numbers in the index
        chap_key = self.get_chapter(index=index)

        pass


icd = Icd()
icd.make_block()
tree = icd.make_tree_dig()
print(icd.codes["B00-B09"])
# icd.match_index(index="R80")
print(icd.get_chapter(index="A30"))

# ICD_PATH = data_path / 'raw/codes/icd-10-se-2021-text'
# file_path = ICD_PATH / 'digit3.txt'

# ICD000 = []
# with open(ICD_PATH / 'digit3.txt','r') as codes:
#     for line in codes:
#         x = re.split(ddd, line)
#         ICD000.append(x[1].strip())

# ICD0000 = []
# with open(ICD_PATH / 'digit4.txt','r') as codes:
#     for line in codes:
#         x = re.split(dddd, line)
#         ICD0000.append(x[1].strip())

# ICD00000 = []
# with open(ICD_PATH / 'digit5.txt','r') as codes:
#     for line in codes:
#         x = re.split(ddddd, line)
#         ICD00000.append(x[1])

# ICD = ICD000 + ICD0000 + ICD00000

# print(f"This file is here: {file_path}")

# import re

# regex_ddd = '/(?<=\D\d\d)\s+?.?\s/gm'
# regex_dddR = '/(?<=R\d\d)\s+?.?\s/gm'
# ddd = r'(?<=\D\d\d)\s+?.?\s'
# dddd = r'(?<=\D\d\d\d)\s+?.?\s'
# ddddd = r'((?<=\D\d\d\d\d)|(?<=\D\d\d\d\D))\s+?.?\s'

# '''
# A513B	†	Syfilitisk (sekundär) alopeci (L99.8)
# Y3498		Ospecificerad skadehändelse, med oklar avsikt-plats, ospecificerad-andra specificerade aktiviteter
# Y3499		Ospecificerad skadehändelse, med oklar avsikt-plats, ospecificerad-aktivitet, ospecificerad
# Y586A		Komplikation av vaccin mot kikhosta, enbart (P)
# Y586B		Komplikation av vaccin mot difteri, kikhosta och stelkramp, kombinerat (DPT)
# Y586W		Komplikation av annat kombinerat
# '''

