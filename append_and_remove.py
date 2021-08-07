#!/usr/bin/env python3

#adding and removing elements from a list.
# we can also build lists, first let's start with an empty one

people = []
people.append("Mattan")
people.append("Sarah")
people.append("Chris")

# now we can print them out too
print(people)

# and remove some
people.remove("Sarah")
print(people)

for person in people:
    print("Person is:", person)
