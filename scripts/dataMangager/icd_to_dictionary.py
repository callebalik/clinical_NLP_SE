import pandas as pd
import re
from pathlib import Path
import re
from tabulate import tabulate

file_path = Path(__file__).resolve()

ROOT = file_path.parent.parent.parent
print(ROOT)
DATA_PATH = ROOT / 'data'
ICD_PATH = DATA_PATH / 'raw/codes/icd-10-se-2021-text'


# patterns to spilt by to separate codes from text
regex_ddd = '/(?<=\D\d\d)\s+?.?\s/gm'
regex_dddR = '/(?<=R\d\d)\s+?.?\s/gm'
ddd = r'(?<=\D\d\d)\s+?.?\s'
dddd = r'(?<=\D\d\d\d)\s+?.?\s'
ddddd = r'((?<=\D\d\d\d\d)|(?<=\D\d\d\d\D))\s+?.?\s'

# Split parenthesis and more in texts
# Blödning från luftvägarna
# Smärta och värk som ej klassificeras på annan plats

'''
Here we would like to only use the text before the comma


A15 Tuberkulos i andningsorganen, bakteriologiskt och histologiskt verifierad
A16 Tuberkulos i andningsorganen, ej verifierad bakteriologiskt eller histologiskt

Dyslexi (lässvårigheter) och andra symboldysfunktioner som ej klassificeras på annan plats
Ascites (vätska i buken)
 - text + parenthesis will probably never be matched
 - "och andra ...." will probably not be written

Positiv HIV-serologi utan säker infektion med humant immunbristvirus [HIV]
    - [HIV]
    - "utan...."

Andra förändringar i huden
Annan koordinationsrubbning
    -"annan..."

R32		Ospecificerad urininkontinens
R33		Urinretention (urinstämma)

Let's create alternation so that the parts can be matched
'''
reComma = r''
reInParenthesis = r''
reWithoutParenthesis = r''
reTrailingAnd = r''
reTrailingWithout = r''
reBeginningOther = r''
reFacingUnspecified = r''

ic = {}


with open(ICD_PATH / 'digit3.txt','r', encoding='utf-8') as codes:
     for line in codes:
         icd_data = re.split(ddd, line)
         code = icd_data[0]
         cat = code[0]
         text = icd_data[1].strip()
       #  alternations = re.split(, text)
        # alternations =
         if cat in ic:
             ic[cat][code] = {'text': text, 'alternations': 'Janitor'}
         else:
             ic[cat] = {}
             ic[cat][code] = {'text': text, 'alternations': 'Janitor'}


print(ic["R"])




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




# df = pd.DataFrame.from_dict({(i,j): ic[i][j]
#                            for i in ic.keys()
#                            for j in ic[i].keys()},
#                        orient='index')

# print(tabulate(df, tablefmt='psql'))