#!/usr/bin/env python3

class Pet(object):


    def __init__(self, name = ""):
        self.name = name
        self.kind = ""
        self.toys = []

    def add_toy(self, toy):
        if toy in self.toys:
            pass
        else:
            self.toys.append(toy)

    def __str__(self):
        toy_line = ""
        if self.toys == []:
            frase = "{} är en {} som inte har några leksaker."
        else:
            frase = "{} är en {} som har följande leksaker: {}"
            for element in self.toys:
                if element == self.toys[-1]:
                    toy_line = toy_line + element + "."
                else:
                    toy_line = toy_line + element + ", "
        return frase.format(self.name, self.kind, toy_line)
