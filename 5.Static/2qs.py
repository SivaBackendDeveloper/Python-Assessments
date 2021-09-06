#Define a static variable and access that through a instance

class myclass:
    #static variable
    a=10
    b=20
    #instance method
    def funin(self):
        print("hi")
        print(myclass.a+myclass.b)

mc=myclass()
mc.funin()

