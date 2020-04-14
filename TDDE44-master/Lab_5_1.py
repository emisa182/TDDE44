#!/usr/bin/env python3
import Klasser
Pet = Klasser.Pet


"""Tilldelar variabler t.ex. namn, typ m.m. och kallar på Pet genom print."""

dog = Pet()
djur = [Pet("Sylvester"), Pet("Göran")]
djur[0].kind = "katt"
djur[1].kind = "iller"
dog.kind = "hund"
djur[0].add_toy("garn")
djur[0].add_toy("boll")
djur[0].add_toy("mus")
djur[1].add_toy("vodka")

print(djur[0])
print(dog)
print(djur[1])
