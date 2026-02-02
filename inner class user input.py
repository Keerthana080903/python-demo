class outer:
 def __init__(self):
        self.number_one = int(input("number one:"))
        class inner:
         def __init__(self):
          self.number_two = int(input("number two:"))
         def display(self):
          print("number one:",self.number_one)
         print("number two:",self.number_two)
        return self.number_one + self.number_two
o = outer()
i= outer.inner()
result = i.display(o.number_one)
print("sum is:",result)
    
