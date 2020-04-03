#!/usr/bin/env python3
import random
import Klasser
Vector2D = Klasser.Vector2D

#def test_method():


v1 = Vector2D()
v2 = Vector2D()
v1.x = random.uniform(-100,100)
print(v1.x)
v1.y = random.uniform(-100,100)
v2.x = random.uniform(-100,100)
v2.y = random.uniform(-100,100)
print(v1.get_length())
v2.add(v1)
print(v2.x)
print(v2.y)
v3 = v2.add_to_new(v1)
print(v3.x)
print(v3.y)
print(v1.is_longer_than(v2))
v4 = v1.create_unit_vector()
print(v4.x)
print(v4.y)
print(v4.get_length())
print(str(v2))


#lista = [add, add_to_new, create_unit_vector]
