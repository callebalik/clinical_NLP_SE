"""
Library for icd codes
"""

from pathlib import Path
from typing import Any, Dict, Type
import re as re
import logging
import logging

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent.parent
DATA_PATH = ROOT / "data"
ICD_PATH = DATA_PATH / "raw/medical_codes/icd-10-se-2021-text"


class IndexLengthError(Exception):
    """Custom error message raised when Icd code dosen't start with a letter"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.value} --> {self.message}"  # Using f-string to format, it's great. Have a look here https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python


class NoIcdLetterSpecification(Exception):
    """Custom error message that is raised when icd code index is to short"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f"{self.value} --> {self.message}"  # Using f-string to format, it's great. Have a look here https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python


class Icd10:
    """block <-> description
          blocks 2 numbers
              3 digit
                  4 digit
                      5 digit
    We want to be able to pass the code e.g. B995 and return the value
    we also want to be able to get all codes in a certain range and specificity
    """

    def __init__(self) -> None:
        self.blocks = {}
        self.level3 = {}
        self.level4 = {}
        self.level5 = {}
        # Must be run sequentially
        self.make_block()
        self.make_codes(3)
        self.make_codes(4)
        self.make_codes(5)

    def make_block(self) -> None:
        with open(
            ICD_PATH / "block.txt", mode="r", encoding="utf-8-sig"
        ) as blocks:  # Giving the correct encoding, the BOM is omitted in the result: \ufefftest'
            for block in blocks:
                block = re.split(r"$\s", block)  # remove trailing whitespace
                block = re.split(
                    r"(?<=\w\d\d)\s+", block[0]
                )  # split block codes from text

                # Set start end and text in a list as values for the corresponing key
                self.blocks[block[0]] = {"text": block[1]}

    def make_codes(self, level: int) -> None:
        path = (
            ICD_PATH / f"digit{str(level)}.txt"
        )  # Get path to file with the codes for the specifided level

        re_index = re.compile(r"^\w\d+\w?")  # get code: A112B.
        re_text = re.compile(r"(?<=[\r\t\f])\S(?=\S).+")  # Get text
        re_special = re.compile(r"(?<=\s)\W(?=\s)")  # Gets special sign

        with open(path, mode="r", encoding="utf-8-sig") as icd_doc:

            for row in icd_doc:

                index = re_index.search(row).group()
                IcdCode.validate_index(index)

                text = re_text.search(row).group()
                special = re_special.search(row)

                code = IcdCode(
                    re_index.search(row).group(),
                    re_text.search(row).group(),
                    re_special.search(row),
                )  # Constructs a icdcode object that validates the index

                parent = self.get_parent(index)  # Get's parent node
                # parent[index] = {"text": text, "special": special}

                if level > 3:
                    parent.children[code.index] = code
                else:
                    parent[code.index] = code

    def get_code(self, index: str):
        IcdCode.validate_index(index)

        block = self.get_block(index)

        node = block[index[0:3]]  # Gets first 3 specifiers in index

        if node.index != index:
            node = node.children[index[0:4]]
            if node.index != index:
                node = node.children[index[0:5]]  # Gets the child with 5 specifiers

        return node

    def get_block(self, index: str):
        IcdCode.validate_index(index)

        key_list = list(self.blocks)
        last_key = ""

        for key in key_list:
            if index < self.get_block_start(
                key
            ):  # compare block end to index, if index < end, then it's in that block
                return self.blocks[last_key]

            last_key = key

            if key == key_list[len(key_list) - 1]:  # special for last block
                return self.blocks[key]

    def get_block_start(self, block: str) -> str:
        index_start = re.split(
            r"(?<=\d)-(?=\D)", block
        )  # split start end end of code at - e.g. A30-A49
        return index_start[0]

    def get_block_end(self, block: str) -> str:
        index_end = re.split(
            r"(?<=\d)-(?=\D)", block
        )  # split start end end of code at - e.g. A30-A49
        return index_end[1]

    def get_children(self, index: str):
        """Gets all children of the given index"""
        return self.get_code(index).children

    def get_parent(self, index: str):

        if (
            len(index) == 3
        ):  # The parent is a block. note (IcdCode) already vailidates that the index is lengt 3:5
            return self.get_block(index)

        return self.get_code(
            index[0 : len(index) - 1]
        )  # Get's the node above index=A4345 -> index[0:len...] = A434


class IcdCode:
    """
    Through the use of optional sub-classifications, ICD-10 allows for specificity regarding the cause, manifestation, location, severity, and type of injury or disease.
    """

    index: str
    text: str
    special: Any
    children: Dict
    parent: Any

    def __init__(self, index: str, text: str, special):
        IcdCode.validate_index(index)
        self.index = index
        self.text = text

        if special == None:
            self.special = None
        else:
            self.special = special

        self.children = {}

    @staticmethod
    def validate_index_length(index: str):
        if len(index) < 3 or len(index) > 5:
            raise IndexLengthError(
                value=index,
                message="Icd code should begin with a letter followed by up to 4 nr or 3 nr and a letter in last position",
            )

    @staticmethod
    def validate_index_letter(index: str):
        if not index[0].isalpha():
            raise NoIcdLetterSpecification(
                value=index, message="Icd codes should begin with a letter"
            )

    @staticmethod
    def validate_index(index: str):
        IcdCode.validate_index_letter(index)
        IcdCode.validate_index_length(index)

    def get_info(self):
        pass


class IcdBlock:

    block_start: str
    block_end: str
    text: str
    children: Dict

    def __init__(self, block: str, text: str):
        self.block_start = self.get_block_start(block)
        self.block_end = self.get_block_end(block)
        self.text = text
        self.children = {}

    @staticmethod
    def get_block_start(self, block: str) -> str:
        index_start = re.split(
            r"(?<=\d)-(?=\D)", block
        )  # split start end end of code at - e.g. A30-A49
        return index_start[0]

    @staticmethod
    def get_block_end(block: str) -> str:
        index_end = re.split(
            r"(?<=\d)-(?=\D)", block
        )  # split start end end of code at - e.g. A30-A49
        return index_end[1]

    # def get_block_text(self, index=str) -> str:
    #     """Get the text for the block of a given index"""
    #     block_key = self.get_block(index=index)
    #     return self.codes[block_key][2]  # block text


def main() -> None:  # The -> None is optional and just for type checking
    """Main function."""
    icd10 = Icd10()
    a = icd10.get_code("A022")
    icd10.get_children("A15")


if __name__ == "__main__":  # When you just want to run the main method
    main()
