import random
from abc import ABC, abstractmethod

class Parent(ABC):
    def __init__(self, blood: str):
        if len(blood) != 2:
            raise ValueError("Blood type must be one or two alleles")
        self.blood = blood
    
    @abstractmethod
    def blood_alleles(self):
        pass

class Father(Parent):
    def blood_alleles(self):
        return list(self.blood)
    
class Mother(Parent):
    def blood_alleles(self):
        return list(self.blood)

class Child:
    def __init__(self, father: Father, mother: Mother):
        self.father = father
        self.mother = mother
        self.blood = self.inherit()

    def inherit(self):
        father_alleles = self.father.blood_alleles()
        mother_alleles = self.mother.blood_alleles()
        return random.choice(father_alleles) + random.choice(mother_alleles)

    def __repr__(self):
        return f"Child's blood type: {self.blood}"
    
Bapak = Father("AO")
Ibu = Mother("BO")

Anak = Child(Bapak, Ibu)
print(Anak)