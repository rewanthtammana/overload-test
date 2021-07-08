import myclass

def new(myclass):
    return "overloaded printing = " + myclass.x

myclass.Random.__str__ = new

print(myclass.Random())