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

def load_text(argsys[1]):
    text = open(argsys[1])



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
