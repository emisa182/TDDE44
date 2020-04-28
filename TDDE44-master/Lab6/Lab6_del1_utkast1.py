#!/usr/bin/env python3

with open("lorem.txt", "r") as file:
    data = file.read()


class Token(object):

    def __init__(self, value):
        self.value = value

    def return_length_of_value(self):
        return len(self.value)

    def __str__(self):
        word = "{}"
        return word.format(self.value)


class Sentence(object):

    def __init__(self, value):
        self.value = value
        self.token_list = self.value.split(" ")

    def create_Token_instance(self):
        len_sentence = 0
        for element in self.token_list:
            token = Token(element)
            len_sentence += token.return_length_of_value()
#            len_element += len(element)
        return len_sentence

    def space_finder(self):
        spaces = 0
        for sign in self.value:
            if sign == " ":
                spaces += 1
        return spaces

    def signs(self):
        for word in self.token_list:
            token = Token(element)

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
        print(len(sentence_list))
        return sentence_list

    def dot_finder(self):
        """Räkna antalet punkter (motsvarande meningar)."""
        dots = 0
        for sign in self.value:
            if sign == ".":
                dots += 1
        print(dots)
        return dots

    def words(self):
        word_amount = 0
        sentence_list = create_Sentence_instance()
        for element in sentence_list:
            sentence = Sentence(element)
            word_amount += sentence.space_finder()
        return word_amount
#    def space_finder(self, value):
#        word_counter = 0

#        string = value.replace("\n", " ")

#        for element in string:
#            if element == " ":
#                word_counter += 1

#        signs = len(string) - word_counter

#        sentence_counter = 0
#        for element in string:
#            if element == ".":
#                sentence_counter += 1

#        return signs, word_counter, sentence_counter

    def __str__(self):
        sentences = dot_finder()
        words = words()

        #signs, words, sentences = self.space_finder(self.value)
        str = "Texten innehåller {} meningar.\nTexten innehåller {} \
                ord/skiljetecken.\nTexten innehåller {} tecken."
        return str.format(sentences, words, signs)

if __name__ == "__main__":
    text = Text(data)
    print(text)
