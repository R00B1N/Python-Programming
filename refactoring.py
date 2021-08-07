#!/usr/bin/env python3

answer = input("Do you want to hear a joke? ")


if "y" in answer.lower():
    print("I'm against picketing, but I don't know how to show it.")
    # Mitch Hedburg (RIP)
elif "n" in answer.lower():
    print("Fine.")
else:
    print("I don't understand.")
