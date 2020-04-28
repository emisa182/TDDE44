#!/usr/bin/env python3

with open("lorem.txt", "r") as file:
    data = file.read()


class Text(object):
    """Tittar på hela texten."""

    def __init__(self, value):
        self.value = value
        self.sentence_list = self.value.split("\n")
        del self.sentence_list[-1]              # tar bort överflödigt element.

    def get_num_sentences(self):
        return len(self.sentence_list)

    def get_more(self):
        words = 0
        chars = 0
        for sentence in self.sentence_list:
            line = Sentence(sentence)
            words += line.get_num_tokens()
            chars += line.chars_in_sentence()
        return [words, chars]

    def __str__(self):
        list = self.get_more()
        sentences = self.get_num_sentences()
        str = "Texten innehåller {} meningar.\nTexten innehåller {} " \
            "ord/skiljetecken.\nTexten innehåller {} tecken."
        return str.format(sentences, list[0], list[1])


class Sentence(object):
    """Tittar på meningar."""

    def __init__(self, value):
        self.value = value
        self.token_list = self.value.split(" ")

    def get_num_tokens(self):
        """Räkna antal ord i en mening."""
        return len(self.token_list)

    def chars_in_sentence(self):
        """Räkna antal tecken i en mening."""
        chars = 0
        for token in self.token_list:
            word = Token(token)
            chars += word.get_num_chars()
        return chars


class Token(object):
    """Tar in ett ord eller skiljetecken och skapar instansen value."""

    def __init__(self, value):
        """Definiera value."""
        self.value = value

    def get_num_chars(self):
        """Räkna antal tecken i ord."""
        return len(self.value)


if __name__ == "__main__":
    text = Text(data)
    print(text)
