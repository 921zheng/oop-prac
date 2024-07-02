class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def set_age(self,age):
        self.age=age

d=Dog("Tim", 32)
print(d.get_age())
print(d.get_name())
d.set_age=22
print(d.set_age)