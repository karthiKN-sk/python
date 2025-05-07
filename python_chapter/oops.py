from modules.math_utils import add,subtract



class Person:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"My name is {self.name}, and I am {self.age} years old"
    


p1 = Person(name="Karthi",age=30)
print(p1.greet())


### Encapsulation
# Encapsulation means hiding the internal state of an object and requiring all interaction to be performed through methods.

class BankAccount:
    def __init__(self,owner,balance):
        self.owner = owner
        self.__balance = balance

    def deposit (self,amount):
        if amount > 0:
            self.__balance += amount

    def get_balance(self):
        return self.__balance
    

acc = BankAccount("Karthi",1000)
acc.deposit(500)

print(acc.get_balance())
print(acc.deposit(2000))
print(acc.get_balance())


### Inheritance - Reuse and extend behavior
# Child classes can inherit attributes and methods from parent classes.


class Animal:
    def speak(self):
        return "Some generic sound"
    
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow"
    
b = Animal()    
d = Dog()
c = Cat()

print(b.speak())
print(d.speak())
print(c.speak())





### Polymorphism — One interface, multiple implementations
# Polymorphism allows you to call the same method on different objects, and they respond in their own way.

class PaymentProcessor:
    def pay(self,amount):
        raise NotImplementedError("Subclass must implemented pay method")
    
class PayPal(PaymentProcessor):
    def pay(self, amount):
        return f"Paid ${amount} using PayPal"
    
class Stripe(PaymentProcessor):
    def pay(self, amount):
        return f"Paid ${amount} using Stripe"
    
def checkout(processor: PaymentProcessor, amount: float):
    print(processor.pay(amount))



checkout (PayPal(),250)
checkout(Stripe(),150)



#Bonus: Class vs Instance Variables

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1
        self.instance_id = Counter.count

c1 = Counter()
c2 = Counter()

print(c1.instance_id)
print(c2.instance_id)



##  Packages - Modules
# Importing from Modules (from modules.math_utils import add,subtract)
print(add(10, 5))
print(subtract(10, 5))