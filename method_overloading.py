#Real world example 1
#Finding area of different shapes

class Shape:
    def area(self, length, width = None):
        if width is None:
            return length * length
        else:
            return length * width
        
shape = Shape()
print("The area of a square is: "+ str(shape.area(5)))
print("The area of a rectangle is: "+ str(shape.area(5, 6)))


#Real world example 1
#A user registration system

class UserRegistration:
    def register(self, username, email = None):
        if email:
            return "User " +username +" registered with email " +email
        else:
            return "User " +username +" registered without an email "
        
registration = UserRegistration()
print(registration.register("john_doe"))
print(registration.register("jane_doe", "jane@example.com"))
