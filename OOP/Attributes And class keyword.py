class Cat():
    species='Mammal'
    def __init__(self,breed,age,sports,name):
        self.breed=breed
        self.age=age
        self.sports=sports
        self.name=name
    def meow(self,number):
        print(f"Meow! my name is {self.name} and number is {number}")

my_cat=Cat('Pluffy',3,False,'ham')
print(my_cat.sports)
print(my_cat.age)
print(my_cat.breed)
print(my_cat.species)
my_cat.meow(10)

class circle():
    pi=3.14

    def __init__(self,radius=1):
        self.radius=radius
        self.area=radius*radius*self.pi

    def get_circumference(self):
        return self.radius*self.pi*2

my_circle=circle(20)
print(my_circle.get_circumference())
print(my_circle.area)