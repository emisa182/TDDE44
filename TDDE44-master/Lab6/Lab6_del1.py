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
        self.sentence_list = []
        split_text = value.split("\n")[0:-1]
        for sentence in split_text:
            self.sentence_list.append(Sentence(sentence))

    def get_num_sentences(self):
        """Få antalet meningar i texten."""
        return len(self.sentence_list)

    def __str__(self):
        """Skriv ut hur många meningar, ord och tecken texten består av."""
        token = 0
        chars = 0
        sentences = self.get_num_sentences()

        for element in self.sentence_list:
            token += element.get_num_tokens()
            chars += element.get_chars()

        skriv = "Texten innehåller {} meningar.\nTexten innehåller {} " \
            "ord/skiljetecken.\nTexten innehåller {} tecken."
        return skriv.format(sentences, token, chars)


class Sentence(object):
    """Titta på meningar.

    value -- En mening
    token_list -- Lista med orden i meningen som element
    """

    def __init__(self, value):
        """Deklarera instansvariabler."""
        self.token_list = []
        word_list = value.split(" ")
        for element in word_list:
            self.token_list.append(Token(element))

    def get_num_tokens(self):
        """Räkna antal ord i en mening."""
        return len(self.token_list)

    def get_chars(self):
        """Räkna antal tecken i en mening."""
        chars = 0
        for element in self.token_list:
            chars += element.get_num_chars()
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
