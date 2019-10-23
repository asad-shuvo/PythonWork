class Animal():
    def __init__(self):
        print("Animal Class created")

    def eat(self):
        print("All animal eats")
    def who_i_am(self):
        print("I am an animal")

class cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Cat Class Created")

    def who_i_am(self):
        print("I am a cat")

myAnimal=Animal()
myAnimal.eat()
myAnimal.who_i_am()
myCat=cat()
myCat.eat()
myCat.who_i_am()
