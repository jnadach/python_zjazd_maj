class Animal:
    pass


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Owczarek(Dog):
    pass


# print(issubclass(Cat, Animal))
# print(issubclass(Dog, Animal))
# print(issubclass(Animal, Animal))
# print(issubclass(Cat, Dog))
# print(issubclass(Dog, Cat))
# print(issubclass(Owczarek, Dog))
# print(issubclass(Owczarek, Animal))

# dog = Dog()
#
# print(isinstance(dog, Animal))
# print(isinstance(dog, Dog))
# print(isinstance(dog, Cat))


# dog = Dog()
# dog_1 = Dog()
# dog_2 = dog
#
# print(dog is dog)
# print(dog is dog_1)
# print(dog is dog_2)
# print(dog, dog_1, dog_2)
#
# print(__name__)
