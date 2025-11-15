class Dog:
    def __init__(self, breed, colour,):
        self.breed = breed
        self.colour = colour
    def __init__(self, breed, colour,):
        self.breed = breed
        self.colour = colour    

dog1 = Dog("Labradors", "white")
dog2 = Dog("Golden Retriever", "golden-brown",)
    

print("1st Dog Breed:", dog1.breed)
print("1st Dog Colour", dog1.colour)
print("2nd Dog Breed:", dog2.breed)
print("2nd Dog Colour:",dog2.colour)


class ParentClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello from {self.name}!")

class ChildClass(ParentClass):  # ChildClass inherits from ParentClass
    def __init__(self, name, age):
        super().__init__(name)  # Calls the parent class's __init__ method
        self.age = age

    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Create objects
parent_obj = ParentClass("Alice")
child_obj = ChildClass("Bob", 30)

# Call inherited methods
parent_obj.greet()
child_obj.greet()

# Call child-specific methods
child_obj.introduce()