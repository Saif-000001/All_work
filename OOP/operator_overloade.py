class Person:
    def __init__(self, name , age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team = team
        super().__init__(name, age, height, weight)
    
    # overloade
    def __add__(self, others):
        return self.age + others.age

s = Cricketer('shakib', 36, 5.6, 78, 'BAN')
m = Cricketer('mushi',36, 5.5, 70, 'BAN')

print(s+m)