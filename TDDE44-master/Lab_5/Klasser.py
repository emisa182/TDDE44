#!/usr/bin/env python3


class Pet(object):
    """Skapa instanser av djur.

    name -- Namnet på djuret
    kind -- Typ av djur
    toys -- Djurets leksaker
    """

    def __init__(self, name=""):
        """Deklarera instansvariabler."""
        self.name = name
        self.kind = ""
        self.toys = []

    def add_toy(self, toy):
        """Lägg till ny leksak."""
        if toy not in self.toys:
            self.toys.append(toy)

    def __str__(self):
        """Tilldela kommentarer till instanserna."""
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
    """Skapa och utför beräkningar av vektorer i 2D."""

    def __init__(self, x=0, y=0):
        """Deklarera instansvariabler."""
        self.x = x
        self.y = y

    def get_length(self):
        """Ta fram längden av vektorn."""
        return (self.x**2 + self.y**2)**(1/2)

    def add(self, v_1):
        """Addera en vektor till en annan."""
        self.x = self.x + v_1.x
        self.y = self.y + v_1.y
        return self.x, self.y

    def add_to_new(self, v_1):
        """Addera 2 vektorer till en ny vektor."""
        new_vector = Vector2D()
        new_vector.x = self.x + v_1.x
        new_vector.y = self.y + v_1.y
        return new_vector

    def is_longer_than(self, v_1):
        """Jämför om en vektor är längre än en annan."""
        return self.get_length() < v_1.get_length()

    def create_unit_vector(self):
        """Skapa en enhetsvektor."""
        new_vector = Vector2D()
        new_vector.y = self.y * ((self.x**2 + self.y**2)**(-1/2))
        new_vector.x = self.x * ((self.x**2 + self.y**2)**(-1/2))
        return new_vector

    def __str__(self):
        """Förklara vektorn."""
        frase = "Vektor med koordinaterna ({},{}). "
        return frase.format(self.x, self.y)
