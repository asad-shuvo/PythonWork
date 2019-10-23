class Animal():
    def __init__(self,name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")
class cat(Animal):
        def speak(self):
            return self.name+" says meow"

class dog(Animal):
    def speak(self):
        return self.name + " says woof"


fidp=dog('fido')
isis=cat('isis')

print(fidp.speak())
print(isis.speak())