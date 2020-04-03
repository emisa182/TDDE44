#!/usr/bin/env python3
import Klasser

Pet = Klasser.Pet

dog = Pet()
cat = Pet("Sylvester")
illern = Pet("Göran")
cat.kind = "tiger"
illern.kind = "iller"
dog.kind = "varg"
cat.add_toy("garn")
cat.add_toy("knark")
cat.add_toy("knark")
illern.add_toy("vodka")

print(str(dog))
print(str(cat))
print(str(illern))
