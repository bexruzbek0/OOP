
class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)  
        self.sound = "Woof"      


dog1 = Dog("Rex")


print("Itning nomi:", dog1.name)
print("Itning tovushi:", dog1.sound)
