#!/usr/bin/env python3
import random
import Klasser
Vector2D = Klasser.Vector2D

# def test_method():

"""Tilldelning av diverse variabler"""

v1 = Vector2D()
v2 = Vector2D()
v1.x = random.uniform(-100, 100)
v1.y = random.uniform(-100, 100)
v2.x = random.uniform(-100, 100)
v2.y = random.uniform(-100, 100)

after = "Resultat: {}"


"""Test av Vector2D"""

print("\n")


def test_get_length(vector):
    print("Running: get_length")
    before = "Instansens innehåll innan metoden: Vektorn ({},{})"
    print(before.format(vector.x, vector.y))
    after = "Längd på vektor: {}"
    print(after.format(vector.get_length()))


test_get_length(v2)


print("\n")


def test_add(v1, v2):
    print("Running: add")
    before = "Vi adderar vektorn ({},{}) till vår vektor ({},{})"
    print(before.format(v1.x, v1.y, v2.x, v2.y))
    after = "Nya koordinater på vår vektor: ({},{})"
    v2.add(v1)
    print(after.format(v2.x, v2.y))
    return v2


test_add(v1, v2)


print("\n")


def test_add_to_new(v1, v2):
    print("Running: add_to_new")
    before = "Vi adderar vektorn ({},{}) med vektorn ({},{})"
    print(before.format(v1.x, v1.y, v2.x, v2.y))
    after = "Den nya vektorns koordinater: ({},{})"
    v3 = v2.add_to_new(v1)
    print(after.format(v3.x, v3.y))
    return v3


test_add_to_new(v1, v2)


print("\n")


def test_is_longer_than(v1, v2):
    print("Running: is_longer_than")
    before = "Vi jämför om vektorn ({},{}) är längre än vektorn ({},{})"
    print(before.format(v1.x, v1.y, v2.x, v2.y))
    after = "Resultat: {}"
    print(after.format(v1.is_longer_than(v2)))


test_is_longer_than(v1, v2)


print("\n")


def test_create_unit_vector(v1):
    print("Running: create_unit_vector")
    before = "Vektorn innan normering: ({},{})"
    print(before.format(v1.x, v1.y))
    v4 = v1.create_unit_vector()
    after = ("Enhetsvektorn som skapades är: ({},{})")
    print(after.format(v4.x, v4.y))
    return v4


test_create_unit_vector(v1)


print("\n")


def test__str__(v1):
    print("Running: __str__")
    print(str(v1))


test__str__(v1)
