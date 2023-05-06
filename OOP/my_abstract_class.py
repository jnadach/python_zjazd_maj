from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def __init__(self, value):
        self.value = value
        super().__init__()

    @abstractmethod
    def foo(self):
        pass


class MyClass(AbstractClass):

    def foo(self):
        print(f"Implememnted. Vaue is {self.value}")


my_class = MyClass(11)
my_class.foo

#Metody abstrakcyjne to takie ktore nie maja implementacji
