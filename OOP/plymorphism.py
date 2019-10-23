class dog():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+" says woof"

class cat():
    def __init__(self,name):
        self.name=name
    def speak(self):
        return self.name+" says meow"
def pet_speak(pet):
    print(pet.speak()+ '  in function')
niko=dog('niko')
felix=cat('felix')

print(niko.speak())
print(felix.speak())

for pet in[niko,felix]:
    print(type(pet))
    print(pet.speak())
pet_speak(niko)
pet_speak(felix)
