#!/usr/bin/env python3


class Pet(object):

    def __init__(self, name=""):
        self.name = name
        self.kind = ""
        self.toys = []

    def add_toy(self, toy):
        if toy not in self.toys:
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


class Vector2D(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_length(self):
        return ((self.x**2 + self.y**2)**(1/2))

    def add(self, v1):
        self.x = self.x + v1.x
        self.y = self.y + v1.y
        return self.x, self.y

    def add_to_new(self, v1):
        new_vector = Vector2D()
        new_vector.x = self.x + v1.x
        new_vector.y = self.y + v1.y
        return new_vector

    def is_longer_than(self, v1):
        return self.get_length() < v1.get_length():


    def create_unit_vector(self):
        new_vector = Vector2D()
        new_vector.y = self.y * ((self.x**2 + self.y**2)**(-1/2))
        new_vector.x = self.x * ((self.x**2 + self.y**2)**(-1/2))
        return new_vector

    def __str__(self):
        frase = "Vektor med koordinaterna ({},{}). "
        return frase.format(self.x, self.y)
