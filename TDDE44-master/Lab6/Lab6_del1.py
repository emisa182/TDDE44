#!/usr/bin/env python3

with open("lorem.txt", "r") as file:
    data = file.read()


class Text(object):
    """Titta på hela texten.

    value -- Text
    sentence_list -- Lista med alla meningar i texten som varsitt element
    """

    def __init__(self, value):
        """Deklarera instansvariabler."""
        self.value = value
        self.sentence_list = self.value.split("\n")         # egen
        del self.sentence_list[-1]                          # tar bort överflödigt element.

    def get_num_sentences(self):
        """Få antalet meningar i texten."""
        return len(self.sentence_list)

    def get_more(self):                                     # egen
        """Få antalet ord och tecken i texten."""
        words = 0
        chars = 0
        for sentence in self.sentence_list:
            line = Sentence(sentence)                   # Flytta upp i __init__ då listelementen ska vara instanser av Sentence
            words += line.get_num_tokens()
            chars += line.chars_in_sentence()
        return [words, chars]

    def __str__(self):
        """Skriv ut hur många meningar, ord och tecken texten består av."""
        values = self.get_more()
        sentences = self.get_num_sentences()
        skriv = "Texten innehåller {} meningar.\nTexten innehåller {} " \
            "ord/skiljetecken.\nTexten innehåller {} tecken."
        return skriv.format(sentences, values[0], values[1])


class Sentence(object):
    """Titta på meningar.

    value -- En mening
    token_list -- Lista med orden i meningen som element
    """

    def __init__(self, value):
        """Deklarera instansvariabler."""
        self.value = value
        self.token_list = self.value.split(" ")         # egen, flytta upp chars hit också

    def get_num_tokens(self):
        """Räkna antal ord i en mening."""
        return len(self.token_list)

    def chars_in_sentence(self):                        # egen
        """Räkna antal tecken i en mening."""
        chars = 0
        for token in self.token_list:
            word = Token(token)
            chars += word.get_num_chars()
        return chars


class Token(object):
    """Tar in ett ord eller skiljetecken och skapar instansen value.

    value -- Ett ord eller skiljetecken
    """

    def __init__(self, value):
        """Definiera value."""
        self.value = value

    def get_num_chars(self):
        """Räkna antal tecken i ord."""
        return len(self.value)


if __name__ == "__main__":
    text = Text(data)
    print(text)
