#1. Create an abstract class with abstract and non-abstract methods.

#abc stands for (abstract base class)
from abc import ABC,abstractmethod

class water(ABC):
    #abstract method
    @abstractmethod
    def purpose(self):
        pass

class kinely(water):
    def purpose(self):
        print("it is a international drinking water bottle brand")

obj=kinely()
obj.purpose()
