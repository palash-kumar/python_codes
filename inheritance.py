# Inheritance: When a class inherits the properties and methods of another class
# Parent class: MobileTransaction
# Child class: bkash, nexus
# Overriding: When a child class redefines a method of the parent class
# Polymorphism: When the function name is same but the functionality is different in different classes

class MobileTransaction:
    def __init__(self):
        print(f"This ia parent Class constructor")

    def parent_method(self):
        print("This is parent class method")

    # Polymorphism example Empty parent function therefore child classes must implement this method according to their own requirements
    def send_money():
        pass

class bkash(MobileTransaction):

    # This constructor is overriding the parent class constructor
    def __init__(self):
        print(f"This is Child Class constructor")

    # Overriding parent class method
    def parent_method(self):
        print("This is parent class method")

    # Polymorphism example
    def send_money(self, phone, amount, fee, pin, finger_print):
        print(phone, amount, fee, pin, finger_print)
        print(f"Sending {amount} to {phone} via bkash.")


class nexus(MobileTransaction):

    # This constructor is overriding the parent class constructor
    def __init__(self):
        print(f"This is nexus Class constructor")

    # Overriding parent class method
    def parent_method(self):
        print("This is nexus class method")

    # Polymorphism example
    def send_money(self, phone, amount, fee, pin, otp):
        print(phone, amount, fee, pin, otp)
        print(f"Sending {amount} to {phone} via nexus.")

bkash_obj = bkash()
bkash_obj.parent_method()

bkash_obj.send_money("017XXXXXXXX", 1000, 10, 1234, "finger_print_data")

nexus_obj = nexus()
nexus_obj.parent_method()

nexus_obj.send_money("017XXXXXXXX", 1000, 10, 1234, 1234)


