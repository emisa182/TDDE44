"""Programmet ska kontrollera stavningen på alla ord i en fil,
om ett ord saknas i ordfrekvensdatan ska förslag på ord med de kortaste
redigeringsavstånden som finns med i datan ges. Vi ska även ta tid på hur
lång tid programmet körs, skriva ut information under körning,
samt spara en rapport med förslag på ordersättningar i en textfil.

Rapporten ska innehålla:
Namnet på filen som kontrolleras
Hur lång tid det tar att kontrollera filen
Alla potentiella fel som upptäcks.

För varje potentiellt fel:
Radnummer som felet upptäckts på.
Det potentiellt felstavade ordet.
Minst tre förslag på korrekta ord.

När skriptet körs ska minst följande information skrivas ut:
Efter att ordfrekvensdata har laddats, skriv ut information hur många
    ord som det laddats in frekvenser för, samt från vilken fil som
    informationen laddats in ifrån.
När programmet börjar kontrollera en text, skriv namnet på filen som kontrolleras.
När rapporten sparas, samt namnet på den fil som rapporten sparats i.

        $ python3 erfil.py ordfrekvensdata.tsv filattkontrollera.txt

Att det finns mycket data betyder att ni kan behöva begränsa t.ex.
hur många ord ni slår upp redigeringsavståndet för
att programmet inte ska ta för lång tid på sig.

Använd modulen funktionen time() i modulen time.

ta in textfil via sys

ta in freqfil i metod

vill bryta ner textfilen ord för ord, byta ut punkter mot blanksteg:

*  ta bort dubbelblanksteg till enkelblanksteg
* splittar vid blanksteg och tar bort tomma element eller blankstegssträngar

jämföra textfilens ord



"""
import sys
from med.py import minimum_edit_distance


def load_text(argsys):

    with open(argsys, 'r') as file:
        text = file.read().replace('\n', " ").lower()
    text = text.replace(".", "")
    text = text.replace(",", "")
    list = text.split(" ")
    for word in list:
        if word == "":
            list.remove(word)
    return list


def load_freq_data(filepath):
    """Läs in och returnera frekvensdata från filen med sökvägen filepath.

    Returnerar en lista där varje element i listan är en lista med två element
    med följande struktur: [ord, frekvens]
    """
    file = open(filepath)
    freq_data = []
    for line in file:
        freq_data.append(line.rstrip().split("\t"))
    file.close()
    return freq_data


def word_in_data(word, freq_data):
    """Returnera True om word finns i freq_data, annars returnera False."""
    for word_freq in freq_data:
        if word_freq[0] == word:
            return True
    return False


def find_words_in_file(words, freq_data):
    """Skriv ut om orden i words finns i filen med sökvägen filepath."""
    finns_ej = []
    for word in words:
        #print("{}: {}".format(word, word_in_data(word, freq_data)))

        if word_in_data(word, freq_data) == False:
            finns_ej.append(word)
    return finns_ej


def hitta_ersättningsord(false_list, freq_data):
    for word in false_list:                         # kanske tar för lång tid?
        nya_ord = [["error", 404], ["error", 404], ["error", 404]]
        for element in freq_data:
            nr = minimum_edit_distance(word, element[0])
            for nyttord in nya_ord                             # vill jämföra med listelementen i nya_ord
                if nr < nyttord[1]                          # se över gammal labb för frekvensjämföring av flera element


    [[element, nr], [["och", 13978], 2], [["också", 12896], 1]]
    [[element[0], nr], ["och", 2], ["också", 2]]

def run(argsys1, argsys2):
    words = load_text(argsys2)
    freq_data = load_freq_data(argsys1)
    false_list = find_words_in_file(words, freq_data)


run(sys.argv[1], sys.argv[2])
