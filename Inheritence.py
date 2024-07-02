class Pet:
    def __init__(self, name,age):
        self.name=name
        self.age=age

    def show(self):
        return f'I am {self.name} and I am {self.age}'

class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color=color

    def show(self):
        return f'I am {self.name} and I am {self.age} and I am {self.color}'

class Dog(Pet):
    def bark(self):
        return "woof"
p=Pet("mar",32)
print(p.show())
c=Cat("fds",432,"white")
print(c.show())
d=Dog("sdf",43)
print(d.bark())