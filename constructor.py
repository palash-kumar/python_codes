class Registration:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        print("Registration object created using constructor.")

    def register_user(self):
        # Logic to register the user
        print(f"Registering user: {self.username} with email: {self.email}")

username='Palash'
paswd='palash123'
email='palash@gmail.com'

reg_obj = Registration(username, paswd, email)
reg_obj.register_user()

print(reg_obj.__dir__()) # List all attributes and methods of the object

# ---------------------------------------------
# Arithmetic operations class with constructor
# ---------------------------------------------
from dataclasses import dataclass

@dataclass(order=True) # Using dataclass to simplify class definition
class Arethmatic:
    num1: int
    num2: int

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Division by zero is not allowed."
        
arith_obj = Arethmatic(10, 5)
print("Addition:", arith_obj.add())
print("Subtraction:", arith_obj.subtract())
print("Multiplication:", arith_obj.multiply())
print("Division:", arith_obj.divide())

arith_obj2 = Arethmatic(20, 25)
print("Comparison (arith_obj < arith_obj2):", arith_obj < arith_obj2)

# __rep__() represents the object in string format
# __eq__() equals
# __le__() less than equal to
# __lt__() less than
# __gt__() greater than
# __ge__() greater than equal to
# __ne__() not equal to 