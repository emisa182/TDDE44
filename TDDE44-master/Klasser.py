#!/usr/bin/env python3

class Pet(object):


    def __init__(self, name = ""):
        self.name = name
        self.kind = kind
        self.toys = []

    def add_toy(toy):
        if toy in toys:
            pass
        else:
            toys.append(toy)

#    def __str__(self):






class Contact(object):

    def __init__(self, name):
        self.name = name
        self.phone_num = ""

    def __str__(self):
        citation = "name: {} \nphone number: {}"
        return citation.format(self.name, self.phone_num)

    #def __str__(self):
        #return "{}, {}".format(self.name, self.phone_num)

    def append_to_name(self, string_to_append):
        self.name = self.name + string_to_append
