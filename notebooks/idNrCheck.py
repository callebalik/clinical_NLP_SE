"""
Check correctness of Swedish ID numbers
"""
# ------------
# TAKE THIS IT'S DANGEROUS OUT THERE
# Function names should be lowercase, with words separated by underscores as necessary to improve readability.
# Variable names follow the same convention as function names.
# mixedCase is allowed only in contexts where that's already the prevailing style (e.g. threading.py), to retain backwards compatibility.
# ------------

from typing import List # Just for typechecking of list inputs, optional, but type checking reduces devilish errors

class IdNrLenghtError(Exception):
    """ Custom error message that is raised when idNr dosen't have either 10 or 12 nr """

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.value} --> {self.message}' # Using f-string to format, it's great. Have a look here https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python

class CtrlNrError(Exception):
    """ Custom error message that is raised when ctrlNr isn't divisabale by 10"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.value} --> {self.message}' # Using f-string to format, it's great. Have a look here https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python


# Try to make classes to contain the different parts of what you want to do.
# A Id is a "thing" aka a object, so we want to make it into a class with properties, the most important one being the nr.
# All Id have a list of numbers, or e.g. cars have a speed and a brand


class idNr:

    id_str: str
    id_nr: list

    def __init__(self, id_str): # We pass a idNr to it when we initiaze it
        """ This is a built in method, so called dunder methods __XXXX__ which initializes the class """
        self.id_str = str(id_str) # Here we set the idNr of this specific instance of the class idNr to the specific idNr.

        # Isolate the numbers in input using list comprehension (actually easier than using regex here)
        id_nr = [int(c) for c in self.id_str if c in "0123456789"]
        if len(id_nr) != 10 and len(id_nr) !=12:
            # Raise custom error message - This is really neat for debugging,
            raise IdNrLenghtError(value=self.id_str, message="IdNr should have either 10 or 12 digits")

        self.id_nr = id_nr

    def __repr__(self):
        """ Defines the object reprentation of a given class and will be shown when printing the object if __str__  is not defined    """

        return f'{self.id_nr} is a id nr'

    def validate_date_correctness(self):
        """ Check whether ID has real dates """
        # ToDo implement

    def validate_ctrl_nrbs(self):
        """ Check control numbers - Define what the algorithm is. Should we only use 10 digits even with 12 digit ids?
        In any case this should logically be inside the idNr class as the IdNr holds all the info the function needs. Remember we whant to isolate responsibilites. This function should therefor only do one thing, check wheather the ctrl nbrs are correct. """

        id_nr_multiplied = []

        for i in range(len(self.id_nr)-1):
            digit = self.id_nr[i]
            if ((i+1) % 2) !=0:
                digit = digit * 2
            id_nr_multiplied.append(digit) # We always want to add the digit to the new list, but only multiply if it's odd. So this way we minimize the amount of code. The multiplication is only run for odd nubmers

        # For the control number what you actually want is the last digit
        # It's only one digit so it shouldn't be a list, that's the reason you had to use "sum(kontroll)" in a bit of a akward way before

        ctrl_dig = self.id_nr[len(self.id_nr)-1] # -1 is since index starts at 0 while the lenght or number of items starts at 1.
        # ToDo I would probably move this to the init method so that it's a part of the class. See if you can figure out how using self.xxxx

        # ToDo make into separate function --> high cohesion (Y)
        # Add the shit
        sum = 0

        for digit in id_nr_multiplied:
            if digit > 9:
                sum = sum + digit % 10 + 1 # No need for more checks as the product will always be <= 18
            else:
                sum = sum + digit

        # Test control digit
        if (sum + ctrl_dig) % 10 != 0:
            raise CtrlNrError(value = sum + ctrl_dig, message="The control digit should be divisable by 10")


def main() -> None: # The -> None is optional and just for type checking
     """Main function."""
     # Read input of idNr

     # Create instance (an object) of the class idNr using "xxx" as input

     # id = idNr("8112189874") # Let's set it for testing purpose

     id = idNr(input("personnummer"))
     print(id)
     id.validate_ctrl_nrbs()

if __name__ == '__main__': # When you just want to run the main method
    main()