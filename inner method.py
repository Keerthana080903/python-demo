class outer:
    class inner:
        def add (self, x,y):
            return x+y
x=outer()
y = x.inner()
print(y.add(5,10))


y =("apples")
p =(" oranges")
s =("15 grapes.")
x =(f"The basket is full of {y},{p} and {s}")
print(x)

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def set__name(self,name):
            self.name=name
    def get__name(self):
            return self.name
    def set__age(self,age):
            self.age=age
    def get__age(self):
            return self.age
k =person("keerthana", 22)
print(k.get__name())
print(k.get__age())   