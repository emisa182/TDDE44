#!/usr/bin/env python3
with open("lorem.txt", "r") as file:
    data = file.read()

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


    def create_Token_instance(self):
        len_element = 0
        for element in self.token_list:
            Token(element)
            len_element += len(element)
        print(len_element)


    def __str__(self):
        string = "{}"
        return string.format(self.value)


class Text(object):


    def __init__(self, value):
        self.value = value


    def create_Sentence_instance(self):
        sentence_list = self.value.split("\n")
        for sentence in sentence_list:
            Sentence(sentence)
        return sentence_list


    def space_finder(self, value):
        word_counter = 0

        string = value.replace("\n", " ")

        for element in string:
            if element == " ":
                word_counter += 1

        signs = len(string) - word_counter

        sentence_counter = 0
        for element in string:
            if element == ".":
                sentence_counter += 1



        return signs, word_counter, sentence_counter


    def __str__(self):
        signs, words, sentences = self.space_finder(self.value)
        str = "Texten innehåller {} meningar.\nTexten innehåller {} ord/skiljetecken.\nTexten innehåller {} tecken."
        return str.format(sentences, words, signs)


sentence = Sentence("En lång mening , med skiljetecken .")



text = Text(data)
print(text)
