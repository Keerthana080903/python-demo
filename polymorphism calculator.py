class num1():
    def __init__(self, value):
        self.value = value
        def display(self):
         print("Value:", self.value)
class num2 ():
    def __init__(self, value):
        self.value = value
        def display(self):
         print("Value:", self.value)
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")
if op=='+':
  print ("result",(num1 + num2))
elif op=='-':
 print ("result",(num1 - num2))
elif op=='*':
 print ("result",(num1 * num2))
elif op=='/':
    if num2==0:
     print("error")
    else:
     print ("result",(num1 / num2))      
    
    