class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
    def eat(self):
        print('Vat')

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # overriding
    def eat(self):
        print('vagitabel')

s = Cricketer('shakib', 36, 5.6, 78, 'BD')

s.eat()