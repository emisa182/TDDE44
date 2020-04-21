#!/usr/bin/env python3


class Token(object):


    def __init__(self, value):
        self.value = value


    def __str__(self):
        word = "{}"
        return word.format(self.value)


class Sentence(object):


    def __init__(self, value):
        self.value = value
        self.token_list = self.value.split(" ")

    def create_token_instance(self):
        for element in self.token_list:
            Token(element)
            print(Token(element))

#    def space_finder(self, string):
#        word_counter = 0
#        for element in string:
#            if element == " ":
#                word_counter += 1
#        signs = len(string) - word_counter
#        return signs, word_counter + 1

    def __str__(self):
        string = "Mening {} innehåller {} ord/skiljetecken ({} antal tecken)"
        return string.format(self.value)


class Text(object):


    def __init__(self, value):
        self.value = value


    def read_file(self):
        with open(self.value, "r") as file:
            data = file.read()
        sentence_list = data.split("\n")
        for sentence in sentence_list:
            Sentence(sentence)


    def __str__(self):
        str = "{}"
        return str.format(self.value)

#token = Token("Hej")
#sentence = Sentence("En lång mening , med skiljetecken .")
#sentence.create_token_instance()

text = Text("lorem.txt")
text.read_file()
#text.create_sentence_instance()
