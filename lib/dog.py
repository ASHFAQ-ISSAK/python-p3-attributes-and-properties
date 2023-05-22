#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer",
]


class Dog:
    def __init__(self, name="", breed=""):
        # Check if the name is a valid string
        if not isinstance(name, str):
            print("Name must be a string between 1 and 25 characters.")
            return
        # Check if the name length is valid
        if not 1 <= len(name) <= 25:
            print("Name must be a string between 1 and 25 characters.")
            return
        # Check if the breed is in the approved breeds list
        if not isinstance(breed, str):
            return print("Breed must be in the list of approved breeds.")

        # Set the name and breed of the dog
        self.name = name
        self.breed = breed
