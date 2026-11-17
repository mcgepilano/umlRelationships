class Person: 
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
                return self.__age

person1 = Person("Lina", 20)

print(f"Name: {person1.name}")
print(f"Age: {person1.get_age()}")

#It is better to use getter methods to access private attributes because it allows
#controlled access to the attribute.



