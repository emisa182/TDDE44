#!/usr/bin/env python3
import Klasser
Pet = Klasser.Pet

"""Tilldelar variabler t.ex. namn, typ m.m. och kallar på Pet genom print."""

dog = Pet()
cat = Pet("Sylvester")
illern = Pet("Göran")
cat.kind = "tiger"
illern.kind = "iller"
dog.kind = "varg"
cat.add_toy("garn")
cat.add_toy("boll")
cat.add_toy("mus")
illern.add_toy("vodka")

print(str(dog))
print(str(cat))
print(str(illern))
