#!/usr/bin/env python3

import random

bars = ["Schoolbred's",
"The Wren",
"The Scratcher",
"ACME",
"Blind Barber"]

people = ["Morgan",
"Camila",
"that person you forgot text back",
"Mia",
"John Connor"]

random_bars = random.choice(bars)
random_people = random.choice(people)

if __name__ == '__main__':
    print("How about you go to {} with {}".format(random_bars, random_people))
