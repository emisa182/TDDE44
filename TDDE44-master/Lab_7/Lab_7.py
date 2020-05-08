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

En klass vars instanser är de felaktiga orden - SpellingWarning
En klass som ska känna till alla Spellingwarninginstanser - Report
#En klass som sätter ihop en instans av SpellingWarning med 3 "rättstavade" ord.

Nästa gång:
Vi vill skapa själva rapporten, dvs en textfil.
Vi vill klocka funktionen.
***Vill spara  radnumret som felet upptäcks på***

"""
import sys
from med import minimum_edit_distance


class Readfiles(object):

    def __init__(self, freqpath, textpath):
        with open(textpath, 'r') as file:
            text = file.read().replace('\n', " ").lower()
        text = text.replace(".", "")
        text = text.replace(",", "")
        list = text.split(" ")
        for word in list:
            if word == "":
                list.remove(word)

        self.textlist = list

        file = open(freqpath)
        freq_data = []
        for line in file:
            freq_data.append(line.rstrip().split("\t"))
        file.close()
        self.freqlist = freq_data


class Report(object):

    def __init__(self, argsys1, argsys2):
        self.warninglist = []
        self.files = Readfiles(argsys1, argsys2)
        for word in self.files.textlist:
            if self.word_in_data(word, self.files.freqlist) is False:
                lista = []
                instans = SpellingWarning(word, self.files.freqlist)
                lista.append(instans.word_warning)
                lista.append(instans.word_alternatives)   #trevlig lista med 3 ord
                self.warninglist.append(lista)            # [[felstavat, [förslag1, förslag2, förslag3]], [...
        print(self.warninglist)



    def word_in_data(self, word, freqlist):
        """Returnera True om word finns i freq_data, annars returnera False."""
        for word_freq in freqlist:
            if word_freq[0] == word:
                return True
        return False


class SpellingWarning(object):

    def __init__(self, word_warning, freqlist):
        self.word_warning = word_warning
        self.word_alternatives = self.funktion(freqlist)
        print(str(self.word_warning))

    def funktion(self, freqlist):
        word_suggestions = {}
        for word_alternative in freqlist:
            if len(word_suggestions) < 3:
                word_suggestions[word_alternative[0]] = minimum_edit_distance(self.word_warning, word_alternative[0])

            key_max = max(word_suggestions.keys(), key=(lambda k: word_suggestions[k]))       # måste fatta bättre

            if minimum_edit_distance(self.word_warning, word_alternative[0]) < word_suggestions[key_max]:
                del(word_suggestions[key_max])
                word_suggestions[word_alternative[0]] = minimum_edit_distance(self.word_warning, word_alternative[0])
        return list(word_suggestions.keys())



if __name__ == "__main__":

    Report(sys.argv[1], sys.argv[2])


#my_dict = {'x':500, 'y':5874, 'z': 560}
#key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
#key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

#print('Maximum Value: ',my_dict[key_max])
#print('Minimum Value: ',my_dict[key_min])

#Maximum Value:  5874
#Minimum Value:  500
