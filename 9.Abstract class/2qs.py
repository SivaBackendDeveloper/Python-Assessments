#2. Create a sub class for an abstract class. Create an object in the child class for the abstract class and access the non-abstract methods

from abc import ABC, abstractmethod
#Abstract Class
class Bank(ABC):
   def bank_info(self):
       print("Welcome to bank")
   @abstractmethod
   def interest(self):
       "Abstarct Method"
       pass
#Sub class/ child class of abstract class
class SBI(Bank):
   def balance(self):
       print("Balance is 100")
class Sub1(SBI):
   def interest(self):
       print("In sbi bank interest is 5 rupees")
s= Sub1()
s.bank_info ()
s.balance()
s.interest()