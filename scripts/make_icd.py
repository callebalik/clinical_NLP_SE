"""
module that takes raw icd10 codes and creates a icd object that can be interacted with for studying and modifying icd codes.
"""

from pathlib import Path
from typing import Dict, TypedDict
import re

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent
DATA_PATH = ROOT / 'data'
ICD_PATH = DATA_PATH / 'raw/medical_codes/icd-10-se-2021-text'


    # block <-> description
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
        self.make_block() #! issue i've called it block further down, but is actually block, and block is one level above

    def __repr__(self) -> str:

        pass
    # !issue: get \ufeffA00 for first code, both in block and digit3 file

    def make_block(self) -> None:
        three_dig = {}

        with open(ICD_PATH / 'block.txt', mode='r', encoding="utf-8-sig") as codes: # Giving the correct encoding, the BOM is omitted in the result: \ufefftest'
            for row in codes:
                row = re.split(r'$\s',row) # remove trailing whitespace
                row = re.split(r'(?<=\w\d\d)\s+', row[0]) # split codes from text
                index = row[0]

                # Set start end and text in a list as values for the corresponing key

                self.codes[index] = [row[1], {}]

    def make_three_dig(self) -> None:

        # Lot's of functional repetition here, could be made much better

        with open(ICD_PATH / 'digit3.txt', mode='r', encoding="utf-8-sig") as codes:
            for row in codes:
                row = re.split(r'$\s', row)
                row = re.split(r'(?<=\w\d\d)\s+', row[0])
                # Add all the three dig codes to the list that corresponds to the block [start, end, text, dict_of_three]

                # 1. Get the key to the correct block
                # 2. Add the tree dig codes to their matching blocks in sequence. No sorting needed as that is already done
                self.get_block(row[0])[1][row[0]] = [row[1]]


    def make_four_dig(self) -> None:
        with open(ICD_PATH / 'digit4.txt', mode='r', encoding="utf-8-sig") as codes_four:
            for row in codes_four:
                row = re.split(r'$\s', row) # Trailing whitespace
                row = re.split(r'(?<=\w\d\d\d)\s+', row[0]) # ToDo special cases -- should run to next whitespace followed by text. Also stora extra symbol info

                # if smaller than next three digit index we should add it
                block = self.codes[self.get_block(row[0])]


                if row[0] < row_three[0]: # if the 4 dig is larger than the 3 dig add no more 4 dig to this 3 dig
                    four_dict[row[0]] = row[1] # Create a dictionary for 4 digit codes and their correspodning texts

                    # "A320" <= "A32" -> False. So we have to add one more
                    # print("A099" < "A15") -> true
                    # print("A150" < "A15") -> false
                    # This we can use for the iteratation


    def get_block_start(self, block:str) -> str:
        index_start = re.split(r'(?<=\d)-(?=\D)', block) # split start end end of code at - e.g. A30-A49
        return index_start[0]

    def get_block_end(self, block:str) -> str:
        index_end = re.split(r'(?<=\d)-(?=\D)', block) # split start end end of code at - e.g. A30-A49
        return index_end[1]

    def get_block(self, index:str) -> Dict:
        """ Matches a given code index e.g. B07 to it's correct block parent and returns the key for the block as a str """

        for key in self.codes:
            if self.get_block_end(key) >= index and self.get_block_start(key) <= index:   # compare block end to index, if index < end, then it's in that block
                return self.codes[key]
            # error if we reach end of list without matching, but shouldn't happen in this contained example.

    def get_block_text(self, index=str) -> str:
        """ Get the text for the block of a given index """
        level = len(index) - 1 # Gets the number of numbers in the index

        block_key = self.get_block(index=index)
        return self.codes[block_key][2] # block text

    def get_text(self, index=str) -> str:
        """ Get the text for the specific index """
        level = len(index) - 1 # Gets the number of numbers in the index
        return self.get_block(index=index)[1][index][0]

icd = Icd()
icd.make_block()
tree = icd.make_three_dig()
# icd.match_index(index="R80")
print(icd.get_block(index="A09"))
print(icd.get_text("A09"))
print("end")
# icd.make_tree_to_five_dig()

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

