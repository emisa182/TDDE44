#!/usr/bin/env python3

import random
import math
import sys

def lunchvärmare(eaters):
    heaters = []
    antal_matlådor = len(eaters)
    times = math.ceil(antal_matlådor/2)
    while len(heaters) < times:
        person = random.choice(eaters)
        if person in heaters:
            pass
        else:
            heaters.append(person)
    for person in heaters:
        print("Dagens värmare är: {}".format(person))

lunchvärmare(sys.argv[1:])

print("Hej Benjamin")
