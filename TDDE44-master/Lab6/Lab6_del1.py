#!/usr/bin/env python3

class Token(object):


    def __init__(self, value):
        self.value = value # ord/skiljetecken


    def __str__(self):


class Sentence(object):


    def __init__(self, value):
        self.value = value # meningar


    def __str__(self):



class Text(object):


    def __init__(self, value):
        self.value = value # hela texten

    def __str__(self):


text = Text("Här har vi vår text")
print(str(text))
