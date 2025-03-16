from abc import ABC, abstractmethod

#Abstraksi : Class Character merupakan class abstract yang memiliki method abstract serang
class Character(ABC):
    #Enkapulasi : Atribut nama, hp, attack, dan defense yang disimpan sebagai variable instance
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense
    
    @abstractmethod
    def serang(self, enemy):
        pass

    def bertahan(self):
        self.defense += 10
        print(f"{self.name} bertahan, deff bertambah 10 menjadi {self.defense}")
    
    def heal_hp(self):
        self.hp += 10
        print(f"{self.name} melakukan heal, hp bertambah 10 menjadi {self.hp}")
    
    def info(self):
        print(f"{self.name} HP: {self.hp}, ATT: {self.attack}, DEFF: {self.defense}")

#Pewarisan : Class Hero merupakan subclass dari class Character
class Hero(Character):
    def __init__(self, nama, hp, attack, defense, weapon, item):
        super().__init__(nama, hp, attack, defense)
        self.weapon = weapon
        self.item = item
    
    #Polimorfisme : Method serang yang di override
    def serang(self, enemy):
        print(f"{self.name} menyerang {enemy._nama} dengan {self.weapon.info()}!")
        enemy.recieve_damage(self.attack)
    
    def info(self):
        print(f"{self.name} HP: {self.hp}, ATT: {self.attack}, DEFF: {self.defense}, WEAPON: {self.weapon.info()}, ITEM: {self.item}")
    
    def use_item(self):
        print(f"{self.name} menggunakan {self.item}!")
        if self.item == "Potion":
            self.hp += 10
        elif self.item == "Elixir":
            self.hp += 20
        elif self.item == "Phoenix Down":
            self.hp = 100
        print(f"{self.name} sekarang memiliki {self.hp} HP!")

#Pewarisan : Class Warrior, Mage, dan Archer merupakan subclass dari class Hero
class Warrior(Hero):
    def __init__(self, nama):
        super().__init__(nama, 100, 10, 5, Sword(), "Potion")
    
class Mage(Hero):
    def __init__(self, nama):
        super().__init__(nama, 80, 15, 3, Staff(), "Elixir")

class Archer(Hero):
    def __init__(self, nama):
        super().__init__(nama, 90, 12, 4, Bow(), "Phoenix Down")

#Abstraksi : Class Weapons merupakan class abstract yang memiliki method abstract damage, durability, dan info
class Weapons(ABC):
    @abstractmethod
    def damage(self):
        pass
    
    @abstractmethod
    def durability(self):
        pass
    
    @abstractmethod
    def info(self):
        pass

#Pewarisan : Class Sword, Staff, dan Bow merupakan subclass dari class Weapons
class Sword(Weapons):
    #Enkapulasi : Atribut damage dan durability yang disimpan sebagai atribut private
    def __init__(self):
        self._damage = 10
        self._durability = 100
    
    def damage(self):
        return self._damage
    
    def durability(self):
        return self._durability
    
    def info(self):
        return "Sword (Damage: 10, Durability: 100)"

class Staff(Weapons):
    def __init__(self):
        self._damage = 12
        self._durability = 90
    
    def damage(self):
        return self._damage
    
    def durability(self):
        return self._durability
    
    def info(self):
        return "Staff (Damage: 12, Durability: 90)"

class Bow(Weapons):
    def __init__(self):
        self._damage = 8
        self._durability = 80
    
    def damage(self):
        return self._damage
    
    def durability(self):
        return self._durability
    
    def info(self):
        return "Bow (Damage: 8, Durability: 80)"

#Pewarisan : Class Enemy sebagai lawan dari Hero
class Enemy:
    def __init__(self, nama, hp, attack, defense):
        self._nama = nama
        self._hp = hp
        self._attack = attack
        self._defense = defense
    
    def serang(self, enemy):
        print(f"{self._nama} menyerang {enemy.name}!")
        enemy.hp -= self._attack
        print(f"{enemy.name} menerima {self._attack} damage!")
    
    def recieve_damage(self, damage):
        self._hp -= damage
        print(f"{self._nama} menerima {damage} damage! HP tersisa: {self._hp}")
    
    def info(self):
        print(f"{self._nama} HP: {self._hp}, ATT: {self._attack}, DEFF: {self._defense}")

#Inisialisasi objek
arthur = Warrior("Arthur")
merlin = Mage("Merlin")
robin = Archer("Robin Hood")
enemy = Enemy("Goblin", 50, 5, 0)

#Pemanggilan method
print("Hero:")
arthur.info()
merlin.info()
robin.info()
print("\nEnemy:")
enemy.info()
print()

#Simulasi
arthur.serang(enemy)
merlin.serang(enemy)
robin.serang(enemy)
enemy.serang(arthur)
enemy.serang(merlin)
enemy.serang(robin)
arthur.bertahan()
merlin.heal_hp()
robin.use_item()
arthur.info()
merlin.info()
robin.info()
enemy.info()

