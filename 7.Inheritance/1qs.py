#A, B and C are classes
#A is a super class. B is a sub class of A. C is a sub class of B
#Create three methods in each class, 2 methods are specific to each class and third method (override method) should be in all three Classes A, B and C
#Create a class with main method. Create an object for each class A, B and C in main method and call every method of each class using its own object/instance
#Call an overridden method with super class reference to B and C class’s objects
#Runtime Polymorphism with Data Members/Instance variables, Repeat the above process only for data member


class Bank:
  def name(self):
      print("RBI")
  def location(self):
      print("Delhi")
  def getroi(self):
    return 10;

class SBI(Bank):
  def fullname(self):
      print("State Bank of India")
  def area(self):
      print("Mubai")
  def getroi(self):
    return 7;

class ICICI(Bank):
  def fn(self):
      print("Industrial Credit and Investment Corporation of India")
  def address(self):
      print("Mumbai")
  def getroi(self):
    return 8;

b1=Bank()
b2=SBI()
b3=ICICI()
print(b1.name(),b1.location(),"Bank Rateof interest:",b1.getroi())
print(b2.fullname(),b2.area(),"SBI Rateof interest:",b2.getroi())
print(b3.fn(),b3.address(),"ICICI Rateof interest:",b3.getroi())
