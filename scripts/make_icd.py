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
        self.make_block()
        self.make_three_dig()
        self.make_four_dig()
        self.make_five_dig()

    def __repr__(self) -> str:

        pass

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
                self.get_block(row[0])[1][row[0]] = [row[1], {}]


    def make_four_dig(self) -> None:
        with open(ICD_PATH / 'digit4.txt', mode='r', encoding="utf-8-sig") as codes:
            for row in codes:
                row = re.split(r'$\s', row) # Trailing whitespace
                row = re.split(r'(?<=\w\d\d\d)\s+', row[0]) # ToDo special cases -- should run to next whitespace followed by text. Also stora extra symbol info

                # "A320" <= "A32" -> False. So we have to add one more
                # print("A099" < "A15") -> true
                # print("A150" < "A15") -> false
                # print("A150" < "A16") -> true
                # This we can use for the iteratation
                # -----
                # ERGO: if smaller than next three digit index we should add it
                parent = self.get_parent(index=row[0])
                parent[1][row[0]] = row[1]

    def make_five_dig(self) -> None:
        with open(ICD_PATH / 'digit5.txt', mode='r', encoding="utf-8-sig") as codes:
            for row in codes:
                row = re.split(r'$\s', row) # Trailing whitespace
                row = re.split(r'(?<=\w\d\d\d\d)\s+', row[0]) # ToDo special cases -- should run to next whitespace followed by text. Also stora extra symbol info

                parent = self.get_parent(index=row[0])
                parent[1][row[0]] = row[1]

    def get_block_start(self, block:str) -> str:
        index_start = re.split(r'(?<=\d)-(?=\D)', block) # split start end end of code at - e.g. A30-A49
        return index_start[0]

    def get_block_end(self, block:str) -> str:
        index_end = re.split(r'(?<=\d)-(?=\D)', block) # split start end end of code at - e.g. A30-A49
        return index_end[1]


    def get_block_text(self, index=str) -> str:
        """ Get the text for the block of a given index """
        level = len(index) - 1 # Gets the number of numbers in the index

        block_key = self.get_block(index=index)
        return self.codes[block_key][2] # block text

    def get_text(self, index=str) -> str:
        """ Get the text for the specific index """
        level = len(index) - 1 # Gets the number of numbers in the index
        return self.get_block(index=index)[1][index][0]

    def get_block(self, index:str) -> Dict:
        """ Matches a given code index e.g. B07 to it's correct block parent and returns the key for the block as a str """

        listd = list(self.codes)
        last_key = listd[0]

        for key in self.codes:
            b = self.get_block_start(key)
            if index < self.get_block_start(key):   # compare block end to index, if index < end, then it's in that block
                return self.codes[last_key]

            last_key = key

            if key == listd[len(listd)-1]: # special for last block
                return self.codes[key]

    def get_parent(self, index=str):

        # if it's parent is block needs different method - since these are stored as ranges for the keys
        if len(index) <= 3:
            return self.get_block(index)

        # Now for the nested codes
        return self.search_dddd(index)
        # get block
    def search_dddd(self, index=str) -> Dict:
        dddd = index[0:3]
        block = self.get_block(dddd)[1]

        # get first level
        key_list = list(block)

        for key in block: # Access e.g. {A00, Kolera} - this means we also only iterate trough the block and not all keys
            if index < key: # if the index is smaller than the key then it belongs to the previous one
                return block[last_key] # ToDo extend with different levels
            last_key = key

            if index > key_list[len(key_list)-1]:
                return block[key_list[len(key_list)-1]]

    def search_ddddd(self, index=str) -> Dict:
        ddddd = index[3:4]

        dddd = self.search_dddd(index)
        key_list = list(dddd)


        for key in dddd:
            if index < key: # if the index is smaller than the key then it belongs to the previous one
                return dddd[last_key] # ToDo extend with different levels
            last_key = key

            if index > key_list[len(key_list)-1]:
                return dddd[key_list[len(key_list)-1]]


icd = Icd()
# icd.match_index(index="R80")
# print(icd.get_block(index="A09"))
# print(icd.get_text("A09"))
print(icd.get_parent(index="A000"))
print("tada")

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

