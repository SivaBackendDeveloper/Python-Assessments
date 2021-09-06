#4. Create an instance for the child class in child class and call non-abstract methods

from abc import ABC, abstractmethod

class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        pass

    def land(self):# non abstarct method
        print("All checks completed")

class Jet(Aircraft):

    def fly(self):
        print("My jet is flying")

    def land(self):
        super().land()# calling non- abstract methods
        print("My jet has landed")

obj=Jet()
obj.fly()
obj.land()
