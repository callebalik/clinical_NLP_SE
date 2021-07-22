personnummer = input("personnummer")

riktigt = True
nrriktigt = True

#ta bort onödiga tecken
for char in personnummer:
    personnummer = personnummer.replace("-" ,"")
for char in personnummer:
    personnummer = personnummer.replace(" " ,"")


#kolla mängden siffror
siffertal = len(personnummer)
if siffertal != 12 and siffertal != 10:
    nrriktigt = False


#splitta siffrorna
nummerlista = []
for num in personnummer:
    nummerlista.append(num)

#göra om till integers
#nummerlista = list(map(int, nummerlista))

#splitta till jämna och ojämna och kontroll
even = []
odd = []
kontroll = []
oddin = [-2, -4, -6, -8, -10]
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
oddstring = list(map(int, oddstring))

#addera skiten
slutsiffra = sum(oddstring) + sum(even)

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