"""
Check correctness of Swedish ID numbers
"""

from typing import List # Just for typechecking of list inputs, optional, but type checking reduces devilish errors

class IdNrLenghtError(Exception):
    """ Custom error message that is raised when idNr dosen't have either 10 or 12 nr """

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

    idStr: str
    idNr: list


    def __init__(self, idStr): # We pass a idNr to it when we initiaze it
        """ This is a built in method, so called dunder methods __XXXX__ which initializes the class """
        self.idStr = str(idStr) # Here we set the idNr of this specific instance of the class idNr to the specific idNr.

        # Isolate the numbers in input using list comprehension (actually easier than using regex here)
        idNr = [c for c in self.idStr if c in "0123456789"]
        if len(idNr) != 10 and len(idNr) !=12:
            # Raise custom error message - This is really neat for debugging,
            raise IdNrLenghtError(value=self.idStr, message="IdNr should have either 10 or 12 digits")

        self.idNr = idNr

    def __repr__(self):
        """ Defines the object reprentation of a given class and will be shown when printing the object if __str__  is not defined    """
        return str(self.idNr)





# We don't really need to set these, but can rather look at it as it being true if we don't run into an error
#riktigt = True
# nrriktigt = True

# Now redundant as we aldready clean the data when initiazing the idNr object

#ta bort onödiga tecken
#for digit in idNr:
#    idNr = idNr.replace("-" ,"")
#for digit in idNr:
#    idNr = idNr.replace(" " ,"")


#kolla mängden siffror
# siffertal = len(idNr)
#if siffertal != 12 and siffertal != 10:
#    nrriktigt = False

#It's now already in a list format from reading it in from the IdStr

#splitta siffrorna
#nummerlista = []
#for num in idNr:
#    nummerlista.append(num)

#göra om till integers
#nummerlista = list(map(int, nummerlista))

#splitta till jämna och ojämna och kontroll
even = []
odd = []
kontroll = []
oddin = [-2, -4, -6, -8, -10] # Using the negatives is neat, but the solution as a whole makes the function more dependant on the correct nr of digits in the input
evenin = [-3, -5, -7, -9]
kontrollin = [-1]
for num in oddin:
    odd.append(nummerlista[num])
for num in evenin:
    even.append(nummerlista[num])
for num in kontrollin:
    kontroll.append(nummerlista[num])

#multiplicera udda talen med 2
oddmult = []
for num in odd:
    oddmult.append(num*2)

#gör udda nummer till stringlista
oddmultstr = []
for num in oddmult:
    oddmultstr.append(str(num))

#gör stringlista till string
oddstring = ""
oddstring = oddstring.join(oddmultstr)

#gör oddstring till integerlista
oddstring = list(map(float, oddstring))

#addera skiten
a = sum(oddstring)
b = sum(even)
slutsiffra = a + b

#lägg till kontrollsiffra
slutsiffra = slutsiffra + sum(kontroll)

if slutsiffra % 10 != 0:
    riktigt = False


if nrriktigt == True:
    print("Det är rätt mängd siffror i nummret")
else:
    print("Det är fel mängd siffror i numret")

if riktigt == True:
    print("Kontrollsiffran stämmer")
else:
    print("Kontrollsiffran stämmer inte")




def main() -> None: # The -> None is optional and just for type checking
     """Main function."""
     # Read input of idNr
     id = idNr("451263av545226") # Let's set it for testing purpose
     # idNr = input("personnummer")
     print(id)

if __name__ == '__main__':
    main()