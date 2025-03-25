from abc import ABC, abstractmethod

class Zoo(ABC):
    def __init__(self, name, age):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if age <=0:
            raise ValueError("Age must be greater than zero")
        
        self.__name = name
        self.__age = age

    @abstractmethod
    def make_sound(self):
        pass

    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def set_name(self, name):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        self.__name = name

    def set_age(self, age):
        if age <=0:
            raise ValueError("Age must be greater than zero")
        self.__age = age

class Dog(Zoo):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.__breed = breed

    def make_sound(self):
        return "Bark"

    def get_breed(self):
        return self.__breed
    
    def set_breed(self, breed):
        self.__breed = breed

class Cat(Zoo):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def make_sound(self):
        return "Meow"

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

class Bird(Zoo):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.__species = species

    def make_sound(self):
        return "Chirp"

    def get_species(self):
        return self.__species
    
    def set_species(self, species):
        self.__species = species

class Snake(Zoo):
    def __init__(self, name, age, length):
        super().__init__(name, age)
        self.__length = length

    def make_sound(self):
        return "Hiss"

    def get_length(self):
        return self.__length
    
    def set_length(self, length):
        self.__length = length

class Giraffe(Zoo):
    def __init__(self, name, age, height):
        super().__init__(name, age)
        self.__height = height

    def make_sound(self):
        return "Bleat"

    def get_height(self):
        return self.__height
    
    def set_height(self, height):
        self.__height = height

class Horse(Zoo):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.__color = color

    def make_sound(self):
        return "Neigh"

    def get_color(self):
        return self.__color
    
    def set_color(self, color):
        self.__color = color

class Fish(Zoo):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.__species = species

    def make_sound(self):
        return "Bubble"

    def get_species(self):
        return self.__species
    
    def set_species(self, species):
        self.__species = species

def describe(animal):
    print(f"\nName: {animal.get_name()}")
    print(f"Age: {animal.get_age()}")
    print(f"Sound: {animal.make_sound()}")

    if isinstance(animal, Dog):
        print(f"Breed: {animal.get_breed()}")
    elif isinstance(animal, Cat):
        print(f"Color: {animal.get_color()}")
    elif isinstance(animal, Bird):
        print(f"Species: {animal.get_species()}")
    elif isinstance(animal, Snake):
        print(f"Length: {animal.get_length()} meters")
    elif isinstance(animal, Giraffe):
        print(f"Height: {animal.get_height()} meters")
    elif isinstance(animal, Horse):
        print(f"Color: {animal.get_color()}")
    elif isinstance(animal, Fish):
        print(f"Species: {animal.get_species()}")

def main():
    animals = []
    while True:
        print("\nZoo Management System")
        print("1. Add Animal")
        print("2. Show Animals")
        print("3. Exit")

        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                print("\nAdd Animal")
                print("1. Dog")
                print("2. Cat")
                print("3. Bird")
                print("4. Snake")
                print("5. Giraffe")
                print("6. Horse")
                print("7. Fish")

                try:
                    animal_choice = int(input("Enter choice: "))
                    name = input("Enter name: ").strip()
                    age = int(input("Enter age: "))

                    if animal_choice == 1:
                        breed = input("Enter breed: ")
                        animals.append(Dog(name, age, breed))
                    elif animal_choice == 2:
                        color = input("Enter color: ")
                        animals.append(Cat(name, age, color))
                    elif animal_choice == 3:
                        species = input("Enter species: ")
                        animals.append(Bird(name, age, species))
                    elif animal_choice == 4:
                        length = float(input("Enter length (meters): "))
                        animals.append(Snake(name, age, length))
                    elif animal_choice == 5:
                        height = float(input("Enter height (meters): "))
                        animals.append(Giraffe(name, age, height))
                    elif animal_choice == 6:
                        color = input("Enter color: ")
                        animals.append(Horse(name, age, color))
                    elif animal_choice == 7:
                        species = input("Enter species: ")
                        animals.append(Fish(name, age, species))
                    else:
                        print("Invalid choice")
                except ValueError:
                    print("Invalid input, please enter correct values.")

            elif choice == 2:
                if not animals:
                    print("No animals")
                else:
                    for animal in animals:
                        describe(animal)
            elif choice == 3:
                print("Exiting program...")
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Invalid input, please enter a number.")

if __name__ == "__main__":
    main()