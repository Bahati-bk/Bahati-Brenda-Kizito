#Method resolution Order Example 1
#Employeee Hierarchy

class Employee:
    def role(self):
        return "Employee"
    
class Manager(Employee):
    def role(self):
        return "Manager"
    
class Director(Manager):
    def role(self):
        return "Director"
    
director = Director()
print(director.role())
print(Director.mro())


#Method resolution Order Example 2
#Vehicle Hierarchy

class Vehicle:
    def type(self):
        return "This is a generic vehicle"
    
class Car(Vehicle):
    def type(self):
        return "Car"
    
class Truck(Vehicle):
    def type(self):
        return "Truck"
    
class SportsCar(Car):
    def type(self):
        return "SportsCar" 
    
sports_car = SportsCar()
print(sports_car.type())
print(SportsCar.mro())