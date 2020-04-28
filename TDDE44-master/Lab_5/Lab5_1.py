#!/usr/bin/env python3

from Klasser import Pet


def get_a_dog():
    """Skapa instans."""
    dog = Pet()
    dog.kind = "hund"
    print(dog)


def get_some_pets():
    """Skapa instanser i en lista."""
    djur = [Pet("Sylvester"), Pet("Göran")]
    djur[0].kind = "katt"
    djur[1].kind = "iller"
    djur[0].add_toy("garn")
    djur[0].add_toy("boll")
    djur[0].add_toy("mus")
    djur[1].add_toy("vodka")
    djur[1].add_toy("vodka")
    print(djur[0])
    print(djur[1])


def __main__():
    """Kör skriptet."""
    get_a_dog()
    get_some_pets()


__main__()
