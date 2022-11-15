from email.errors import FirstHeaderLineIsContinuationDefect
import re
import csv

from numpy import char, place
from pip import List

# ------------------------------------ CSV CREATION FOR GRAPH BUILDING IN GEPHI -------------------------------------------------------
# To create the FIRST GRAPH (FIRST CORPORA), use the starting .txt file "chap1-7.txt"
    # Output files: edges17.csv, nodes7_sheet.csv
# To create the SECOND GRAPH (SECOND CORPORA), use the starting .txt file "chap8-14.txt"
    # Output files: edges8_sheet.csv, node8_sheet.csv
# To create the THIRD GRAPH (THIRD CORPORA), use the starting .txt file "chap15.txt"
    # Output files: edges15_sheet, nodes15_sheet_.csv


# Read the txt file as a string
with open("/Users/martinapensalfini/Documents/Digital Texts In Humanities/amicageniale15.txt", encoding="UTF-8") as f:
    corpora = f.read()

# Clean the corpora-string from excessive spaces, tabs and newline
re.sub('\s{2,}', ' ', corpora)
re.sub('\t+', ' ', corpora)
re.sub('\n+', '', corpora)

# Split the corpora in a list of paragraphs (delimiter: \n)
txt = re.split('\n', corpora)

# Now build the graph
# 1) Gather the 'pers-name' in each paragraph and save the string associated to these (= the name of the character) in a list

# List of lists (each second layer list represents a paragraph) -> List of paragraphs
tot_lst = list()
place_list = list()
char_list = list()

# lists for distinguish between characters' communities
primary_char = list()
greco_fam = list()
cerullo_fam = list()
carracci_fam = list()
spagnuolo_fam = list()
peluso_fam = list()
sarratore_fam = list()
cappuccio_fam = list()
scanno_fam = list()
solara_fam = list()
school_fam = list()


for item in txt:
    # Split the paragraph in a list of words (str)
    word_lst = re.split('\s(?!(\w+\-?\w+\"\>)?(\s?\w+\s?\w+){1,2}\<)', item)

    # Clean the word-list from None elements
    word_lst = list(filter(None, word_lst))
    node_lst = list()   # List of all the nodes contained in the paragraph item (from now on considered as a word-list word_lst)
    for word in word_lst:
        # If the word contains one of these strings it is a character/place
        if "pers-name" in word or "place-name" in word:
            node = re.search('[^class=\"]([\S\s]*)', word)
            node_lst.append(node.group(0))
            # We then add the word in the different 'communities'
            if "pers-name" in word:
                char_list.append(node.group(0))
                if "primary" in word:   # The character is either Lila or Lenù
                    primary_char.append(node.group(0))
                elif "Greco" in word:    # The character belongs to the Greco family
                    greco_fam.append(node.group(0))
                elif "Cerullo" in word:   # The character belongs to the Cerullo family
                    cerullo_fam.append(node.group(0))
                elif "Carracci" in word:    # The character belongs to the Carracci family
                    carracci_fam.append(node.group(0))
                elif "Peluso" in word:  # The character belongs to the Peluso family
                    peluso_fam.append(node.group(0))
                elif "Spagnuolo" in word:    # The character belongs to the Spagnuolo family
                    spagnuolo_fam.append(node.group(0))
                elif "Sarratore" in word:    #  The character belongs to the Sarratore family
                    sarratore_fam.append(node.group(0))
                elif "Cappuccio" in word:    #  The character belongs to the Cappuccio family
                    cappuccio_fam.append(node.group(0))
                elif "Solara" in word:    # The character belongs to the Solara family
                    solara_fam.append(node.group(0))
                elif "Scanno" in word:     # The character belongs to the Scanno family
                    scanno_fam.append(node.group(0))
                elif "school" in word:    # The character works at the school (either teacher Oliviero or Ferraro)
                    school_fam.append(node.group(0))

        

    # Update the list of lists
    tot_lst.append(node_lst)


# ==== CREATING THE EDGES SHEET ====
# 2) Create tuples associating the items of each list together
    # Add attributes

tpl_lst1 = list()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        tpl1 = tuple((paragraph[0], paragraph[i]))
        tpl_lst1.append(tpl1)

# 3) Create the csv file from the tuples

with open('/Users/martinapensalfini/Documents/Digital Texts In Humanities/edges15_sheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Source", "Target"])
    for item in tpl_lst1:
        writer.writerow(item)

# ==== CREATING THE NODES SHEET ====
tpl_lst2 = list()
for paragraph in tot_lst:
    for i in range(len(paragraph)):
        if paragraph[i] in char_list:
            if paragraph[i] in primary_char:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Primary Character"))
            elif paragraph[i] in greco_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Greco Family"))
            elif paragraph[i] in cerullo_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Cerullo Family"))
            elif paragraph[i] in carracci_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Carracci Family"))
            elif paragraph[i] in peluso_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Peluso Family"))
            elif paragraph[i] in spagnuolo_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Spagnuolo Family"))
            elif paragraph[i] in sarratore_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Sarratore Family"))
            elif paragraph[i] in cappuccio_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Cappuccio Family"))
            elif paragraph[i] in solara_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Solara Family"))
            elif paragraph[i] in scanno_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Scanno Family"))
            elif paragraph[i] in school_fam:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "School"))
            else:
                tpl2 = tuple(
                    (paragraph[i], paragraph[i], "Character", "Others"))

            tpl_lst2.append(tpl2)

with open('/Users/martinapensalfini/Documents/Digital Texts In Humanities/nodes15_sheet.csv', 'w', encoding='UTF-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Id", "Label", "Type", "Class"])
    for item in tpl_lst2:
        writer.writerow(item)
