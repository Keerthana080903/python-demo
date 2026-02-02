class Mynumbers():
    def __init__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
    
myclass = Mynumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))