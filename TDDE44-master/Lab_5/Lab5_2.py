#!/usr/bin/env python3

import random
from Klasser import Vector2D

V_1 = Vector2D()
V_2 = Vector2D()

V_1.x = random.uniform(-100, 100)
V_1.y = random.uniform(-100, 100)
V_2.x = random.uniform(-100, 100)
V_2.y = random.uniform(-100, 100)


def test_get_length(vector):
    """Ta fram längden av vektorn."""
    print("Running: get_length")
    before = "Instansens innehåll innan metoden: Vektorn ({},{})"
    print(before.format(vector.x, vector.y))
    after = "Längd på vektor: {}"
    print(after.format(vector.get_length()))
    print("\n")


def test_add(v_1, v_2):
    """Addera en vektor till en annan."""
    print("Running: add")
    before = "Vi adderar vektorn ({},{}) till vår vektor ({},{})"
    print(before.format(v_1.x, v_1.y, v_2.x, v_2.y))
    after = "Nya koordinater på vår vektor: ({},{})"
    v_2.add(v_1)
    print(after.format(v_2.x, v_2.y))
    print("\n")
    return v_2


def test_add_to_new(v_1, v_2):
    """Addera 2 vektorer till en ny vektor."""
    print("Running: add_to_new")
    before = "Vi adderar vektorn ({},{}) med vektorn ({},{})"
    print(before.format(v_1.x, v_1.y, v_2.x, v_2.y))
    after = "Den nya vektorns koordinater: ({},{})"
    v_3 = v_2.add_to_new(v_1)
    print(after.format(v_3.x, v_3.y))
    print("\n")
    return v_3


def test_is_longer_than(v_1, v_2):
    """Jämför om en vektor är längre än en annan."""
    print("Running: is_longer_than")
    before = "Vi jämför om vektorn ({},{}) är längre än vektorn ({},{})"
    print(before.format(v_1.x, v_1.y, v_2.x, v_2.y))
    after = "Resultat: {}"
    print(after.format(v_1.is_longer_than(v_2)))
    print("\n")


def test_create_unit_vector(v_1):
    """Skapa en enhetsvektor."""
    print("Running: create_unit_vector")
    before = "Vektorn innan normering: ({},{})"
    print(before.format(v_1.x, v_1.y))
    v_4 = v_1.create_unit_vector()
    after = ("Enhetsvektorn som skapades är: ({},{})")
    print(after.format(v_4.x, v_4.y))
    print("\n")
    return v_4


def test__str__(v_1):
    """Testa __str__ metoden."""
    print("Running: __str__")
    print(str(v_1))


def __main__():
    """Kör igenom skriptet."""
    test_get_length(V_2)
    test_add(V_1, V_2)
    test_add_to_new(V_1, V_2)
    test_is_longer_than(V_1, V_2)
    test_create_unit_vector(V_1)
    test__str__(V_1)


__main__()
