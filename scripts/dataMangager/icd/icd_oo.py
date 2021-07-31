"""
Library for icd codes
"""

from pathlib import Path
from typing import Any, Dict
import re as re
import codecs

file_path = Path(__file__).resolve()
ROOT = file_path.parent.parent.parent.parent
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

    # icd10_dict = Dict

    def __init__(self) -> None:
        self.icd10_dict = {}
        self.make_codes(3)
        self.make_codes(4)
        self.make_codes(5)

    def make_codes(self, level: int):
        path = (
            ICD_PATH / f"digit{str(level)}.txt"
        )  # Get path to file with the codes for the specifided level

        with open(path, mode="r", encoding="utf-8-sig") as codes:
            for row in codes:
                code = re.search(r"^\w\d+\w?", row)  # get code: A112B
                text = re.search(r"(?<=[\r\t\f])\S(?=\S).+", row)
                special = re.search(r"(?<=\s)\W(?=\s)", row)
                if special != None:
                    special = special.group()
                self.icd10_dict[code.group()] = [text.group(), special]

    def get_code(self, index: str):
        return self.icd10_dict[index]


class IcdCode:
    """
    Through the use of optional sub-classifications, ICD-10 allows for specificity regarding the cause, manifestation, location, severity, and type of injury or disease.
    """

    index: str
    level: int
    block: Any
    text: str
    parent: Any

    def __init__(self, index):
        self.validate_index_letter(index)
        self.validate_index_length(index)

        self.index = index
        self.level = len(index)  # The hirearchical level describes the specificity

    def validate_index_length(self, index: str):
        if len(index) < 3 or len(index) > 5:
            raise IndexLengthError(
                value=self.index,
                message="Icd code should begin with a letter followed by up to 4 nr or 3 nr and a letter in last position",
            )

    def validate_index_letter(self, index: str):
        if index[0].isalpha():
            raise NoIcdLetterSpecification(
                value=self.index, message="Icd codes should begin with a letter"
            )

    def get_info(self):
        pass


class IcdBlock:

    pass


def main() -> None:  # The -> None is optional and just for type checking
    """Main function."""
    icd10 = Icd10()
    a = icd10.get_code("A022")


if __name__ == "__main__":  # When you just want to run the main method
    main()
