#3. Create an instance for the child class in child class and call abstract methods

from abc import ABC, abstractmethod

class Aircraft(ABC):

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        print("All checks completed")

class Jet(Aircraft):

    def fly(self):
        print("My jet is flying")

    def land(self):
        super().land()# calling abstract methods
        print("My jet has landed")

obj=Jet()
obj.fly()
obj.land()
