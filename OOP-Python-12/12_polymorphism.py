class Dog:
    def speak(self):
        print("Dog says: Bark")
class Cat:
    def speak(self):
        print("Cat says: Meow")
dog = Dog()
cat = Cat()

dog.speak()
cat.speak()

# Polymorphism with a Function

class Dog:
    def speak(self):
        print("Bark")

class Cat:
    def speak(self):
        print("Meow")
def animal_sound(animal):
    animal.speak()
dog = Dog()
cat = Cat()

animal_sound(dog)
animal_sound(cat)