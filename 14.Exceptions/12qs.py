#Write a program to generate NoSuchFieldException


class Person:

    # constructor or initializer
    def __init__(self, name):
        self.name = name  # name is data field also commonly known as instance variable

    # method which returns a string
    def whoami(self):
        return "You are " + self.name


try:
    l = [1, "Siva", 318]
    p = Person(l)
    print(p.whoami())
    print(p.name)


except :
    print("NoSuchFieldException ")

