"""
Instantiate an instance of the class Villager, which represents characters in Animal Crossing. 
Store the instance in a variable named apollo.

The Villager object created should have the name "Apollo", the species "Eagle", and 
the catchphrase "pah".
"""
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

# Instantiate your villager here

apollo = Villager("Apollo", "Eagle", "pah")
print(apollo.name)  
print(apollo.species)  
print(apollo.catchphrase) 
print(apollo.furniture) 