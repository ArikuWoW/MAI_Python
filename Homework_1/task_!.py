class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} говорит: {self.sound}")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Мяу")
        self.color = color

    def make_sound(self):
        print(f"{self.name} говорит: Мяу!")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name, "Гав")
        self.color = color

    def make_sound(self):
        print(f"{self.name} говорит: Гав!")

cat = Cat("Белок", "черный")
dog = Dog("Толя", "белый")

cat.make_sound()  
dog.make_sound()  
