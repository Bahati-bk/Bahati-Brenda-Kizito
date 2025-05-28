#Real world example 1
#A payment processing system

class Payment:
    
    def payment_process(self, amount):
        pass
    
class credit_card_payment(Payment):
    def payment_process(self, amount):
        print("You are paying an amount of "+str(amount)+ " using a credit card.")
        return self
        
class cash_payment(Payment):
    def payment_process(self, amount):
        print("You are paying an amount of "+str(amount)+ " using cash.")
        return self
        
class mobile_money_payment(Payment):
    def payment_process(self, amount):
        print("You are paying an amount of "+str(amount)+ " using mobile money.")
        return self
        
payments = [credit_card_payment(), cash_payment(), mobile_money_payment()]
for payment in payments:
    print(payment.payment_process(100))
    
    

#Real world example 2
#Animal sounds
class Animal:
    def sound(self):
        print("This animal makes sound")
        return self
        
class Dog(Animal):
    def sound(self):
        print("The dog barks")
        return self
        
class Cat(Animal):
    def sound(self):
        print("The cat meows")
        return self
        
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())
