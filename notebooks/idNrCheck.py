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

class CtrlNrError(Exception):
    """ Custom error message that is raised when ctrlNr isn't divisabale by 10"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.value} --> {self.message}' # Using f-string to format, it's great. Have a look here https://realpython.com/python-f-strings/#f-strings-a-new-and-improved-way-to-format-strings-in-python


#Day and month class errors

class MonthError(Exception):
    """Error message when month number isnt 01-12"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.value} --> {self.message}'

class DayError(Exception):
    """Error message when day number isnt 01-31"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.value} --> {self.message}'

class DayAndMonthError(Exception):
    """Error message when day and month numbers are incompatible"""

    def __init__(self, value: str, message: str) -> None:
        self.value = value
        self.message = message
        super().__init__(message)

    def __str__(self):
        return f'{self.value} --> {self.message}'


# Try to make classes to contain the different parts of what you want to do.
# A Id is a "thing" aka a object, so we want to make it into a class with properties, the most important one being the nr.
# All Id have a list of numbers, or e.g. cars have a speed and a brand


class idNr:

    idStr: str
    idNr: list
    ctrlNr: str
    monthNr: str
    dayNr: str


    def __init__(self, idStr): # We pass a idNr to it when we initiaze it
        """ This is a built in method, so called dunder methods __XXXX__ which initializes the class """
        self.idStr = str(idStr) # Here we set the idNr of this specific instance of the class idNr to the specific idNr.

        # Isolate the numbers in input using list comprehension (actually easier than using regex here)
        idNr = [int(c) for c in self.idStr if c in "0123456789"]
        if len(idNr) != 10 and len(idNr) !=12:
            # Raise custom error message - This is really neat for debugging,
            raise IdNrLenghtError(value=self.idStr, message="IdNr should have either 10 or 12 digits")
        
        self.idNr = idNr

        # Set controlnumber to the last digit in input

        ctrlNr = self.idStr[-1]

        #Set monthnumber and check monthnumbers

        if len(idNr) ==10:
            monthNr = self.idStr[2:4]
        else:
            monthNr = self.idStr[4:6]

        if int(monthNr) > 12:
            #raise error message
            raise MonthError(value=self.idStr, message="Month number should be between 01-12")

        

        #Set daynumber and check daynumbers

        if len(idNr) ==10:
            dayNr = self.idStr[4:6]
        else:
            dayNr = self.idStr[6:8]
        

        if int(dayNr) > 31:
            #raise error message
            raise DayError(value=self.idStr, message="Day number should be between 01-31")

        #Check if months 4,6,9,11 have more than 30 days and if month 2 has more than 28 days
        if (int(monthNr) == 4 or 6 or 9 or 11) and (int(dayNr) > 30):
            raise DayAndMonthError(value=self.idStr, message="Day and month numbers are incompatible")
        elif (int(monthNr) == 2) and (int(dayNr) >28):
            raise DayAndMonthError(value=self.idStr, message="Day and month numbers are incompatible")

    def __repr__(self):
        """ Defines the object reprentation of a given class and will be shown when printing the object if __str__  is not defined    """

        # We don't really need to set these, but can rather look at it as it being true if we don't run into an error

        #riktigt = True
        # nrriktigt = True

        # if nrriktigt == True:
        #     print("Det är rätt mängd siffror i nummret")
        # else:
        #     print("Det är fel mängd siffror i numret")
        # if riktigt == True:
        #     print("Kontrollsiffran stämmer")
        # else:
        #     print("Kontrollsiffran stämmer inte")

        return str(self.idNr)



    def validate_ctrl_nrbs(self):
        """ Check control numbers - Define what the algorithm is. Should we only use 10 digits even with 12 digit ids?
        In any case this should logically be inside the idNr class as the IdNr holds all the info the function needs. Remember we whant to isolate responsibilites. This function should therefor only do one thing, check wheather the ctrl nbrs are correct. """

          #splitta till jämna och ojämna och kontroll
            # even = []
            # odd = []
            # kontroll = []
            # oddin = [-2, -4, -6, -8, -10] # Using the negatives is neat, but the solution as a whole makes the function more dependant on the correct nr of digits in the input
            # evenin = [-3, -5, -7, -9]
            # kontrollin = [-1]
            # for num in oddin:
            #     odd.append(nummerlista[num])
            # for num in evenin:
            #     even.append(nummerlista[num])
            # for num in kontrollin:
            #     kontroll.append(nummerlista[num])

            #     #multiplicera udda talen med 2
            # oddmult = []
            # for num in odd:
            #     oddmult.append(num*2)

            # #gör udda nummer till stringlista
            # oddmultstr = []
            # for num in oddmult:
            #     oddmultstr.append(str(num))

            # #gör stringlista till string
            # oddstring = ""
            # oddstring = oddstring.join(oddmultstr)

            # #gör oddstring till integerlista
            # oddstring = list(map(float, oddstring))

        # --------------------
        # let's se if we can have a bit more abstracted approach
        # def of even is nr % 2 == 0
        # def of odd is nr % 2 != 0

        ctrlDigs = []


        for i in range(len(self.idNr)-1):
            digit = self.idNr[i]
            if ((i+1) % 2) !=0:
                digit = digit * 2
            ctrlDigs.append(digit) # We always want to add the digit to the new list, but only multiply if it's odd. So this way we minimize the amount of code. The multiplication is only run for odd nubmers
        
        # For the control number what you actually want is the last digit
        # It's only one digit so it shouldn't be a list, that's the reason you had to use "sum(kontroll)" in a bit of a akward way before

        ctrlDig = self.idNr[len(self.idNr)-1] # -1 is since index starts at 0 while the lenght or number of items starts at 1.
        # ToDo I would probably move this to the init method so that it's a part of the class. See if you can figure out how using self.xxxx

        # - ----------
        #addera skiten
        # a = sum(oddstring)
        # b = sum(even)
        # slutsiffra = a + b


        #lägg till kontrollsiffra
        #slutsiffra = slutsiffra + sum(kontroll)

        #if slutsiffra % 10 != 0:
        #   riktigt = False

        # ----------------------
        # try to minimize the amount of code, as it will be way easier to find potential errors and understand

        # add the shit
        sum = 0

        for digit in ctrlDigs:
            if digit > 9:
                sum = sum + digit % 10 + 1 # No need for more checks as the product will always be <= 18
            else:
                sum = sum + digit

        if (sum + ctrlDig) % 10 != 0:
            raise CtrlNrError(value=sum + ctrlDig, message="The control digit should be divisable by 10")


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

def main() -> None: # The -> None is optional and just for type checking
     """Main function."""
     # Read input of idNr
     id = idNr("8112189876") # Let's set it for testing purpose
     # idNr = input("personnummer")
     print(id)
     id.validate_ctrl_nrbs()

if __name__ == '__main__':
    main()