#!/usr/bin/env python3
"""Identifiera eventuellt felstavade ord och ge rättstavningsförslag.

Vi läser in en ordfrekvensdatafil samt ett godtyckligt antal textfiler vilka
kontrolleras mot ordfrekvensdatafilen om ett ord existerar där eller inte.
Därefter skrivs en rapport som beskriver hur lång tid kontrollen tagit samt
vilka ord som är eventuella stavfel. Tillsammans med detta så kommer det
3 förslag på rättstavade ord.
"""

import sys
from time import time
from med import minimum_edit_distance


class Readfile(object):
    """Läs in textfil och ta bort oönskade tecken.

    the_list -- Nästlad lista vars element är rader  med element av ord.
    """

    def __init__(self, textpath):
        """Läs in samt modifiera textfil."""
        with open(textpath, 'r') as file:
            text = file.read().replace('.', "").lower()
            for ch in ['`', '*', '_', '{', '}', '[', ']', '(', ')', '>', '#',
                       '+', ',', '!', '$', '\"', ":", ";", "?"]:
                text = text.replace(ch, "")
            row_list = text.split("\n")
            the_list = []
            for element in row_list:
                word_list = element.split(" ")
                for word in word_list:
                    if word in ("", " ", "–", "-"):
                        word_list.remove(word)
                the_list.append(word_list)
            self.the_list = the_list


class Report(object):
    """Skapa en rapport med de filer som anges.

    warninglist --  En lista med eventuellt felstavat ord, rad som ordet
                    förkommer på i texten samt tre förslag på ersättningsord.
    text_fil -- Den inlästa textfilen i ett lättarbetat format.
    """

    def __init__(self, freq_data, argsys2, start_time):
        """Ta tid på och utför hela rapportskrivningsprocessen, skriv ut."""
        self.warninglist = []
        self.text_file = Readfile(argsys2)
        print("Kontrollerar filen '{}'...".format(argsys2))
        counter = 0
        for row in self.text_file.the_list:
            counter += 1
            for word in row:
                if self.word_in_data(word, freq_data) is False:
                    lista = []
                    instans = SpellingWarning(word, freq_data)
                    lista.append(counter)
                    lista.append(instans.word_warning)
                    lista.append(instans.word_alternatives)
                    self.warninglist.append(lista)            # [[rad, ord, [förslag1, förslag2, förslag3]], [...
        print("Antal eventuellt felstavande ord: {}".
              format(len(self.warninglist)))
        run_time = time() - start_time
        self.write_report(argsys2, round(run_time, 2))

    def word_in_data(self, word, freqlist):
        """Returnera True om word finns i freq_data, annars returnera False."""
        for word_freq in freqlist:
            if word_freq[0] == word:
                return True
        return False

    def write_report(self, textfile, run_time):
        """Skapa textfil och skriv över information."""
        with open("report-" + textfile, "w") as report:
            print("Rapport sparas som '{}'".format(str("report-" + textfile)))
            report.write("Kontroll av '{}' tog {} sekunder.\n\n"
                         .format(textfile, run_time))
            for element in self.warninglist:
                report.write("Rad: {}, {}: {}, {}, {}.\n".format(element[0],
                             element[1], element[2][0], element[2][1],
                             element[2][2]))


class SpellingWarning(object):
    """Hitta förslag till eventuellt felstavade ord.

    word_warning -- det eventuellt felstavade ordet.
    word_alternatives -- lista med förslag till rättstavning av det
                         felstavade ordet
    """

    def __init__(self, word_warning, freqlist):
        """Definiera eventuellt felstavat ord och förslag på rättstavning."""
        self.word_warning = word_warning
        self.word_alternatives = self.funktion(freqlist)

    def funktion(self, freqlist):
        """Ta fram förslag på rättstavning."""
        word_suggestions = {}
        for word_alternative in freqlist[0:1000]:
            if len(word_suggestions) < 3:
                word_suggestions[word_alternative[0]] \
                    = minimum_edit_distance(self.word_warning,
                                            word_alternative[0])

            key_max = max(word_suggestions.keys(),
                          key=(lambda k: word_suggestions[k]))  # fatta bättre

            if minimum_edit_distance(self.word_warning, word_alternative[0])\
                    < word_suggestions[key_max]:
                del(word_suggestions[key_max])
                word_suggestions[word_alternative[0]] \
                    = minimum_edit_distance(self.word_warning,
                                            word_alternative[0])
        return list(word_suggestions.keys())


if __name__ == "__main__":
    start_time = time()                 # Hur bör tidtagning tas?
    print("Antal filer att kontrollera: {}".format(len(sys.argv[2:])))

    file = open(sys.argv[1])
    freq_data = []
    for line in file:
        freq_data.append(line.rstrip().split("\t"))
    file.close()
    frase = "Läser in frekvensdata från filen '{}'...\n\
    Frekvensdata för {} ord har laddats in."
    print(frase.format(sys.argv[1], len(freq_data)))
    for argument in sys.argv[2:]:
        Report(freq_data, argument, start_time)


# my_dict = {'x':500, 'y':5874, 'z': 560}
# key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))
# key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))

# print('Maximum Value: ',my_dict[key_max])
# print('Minimum Value: ',my_dict[key_min])

# Maximum Value:  5874
# Minimum Value:  500
