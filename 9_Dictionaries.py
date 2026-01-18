"""
Problem 1: The "User Login Tracker" (Initialization & Updates)
The Scenario: You are managing a server. You have a dictionary where the Key is the username and the Value is the number of times they have logged in.
The Task: 
1. Create a dictionary login_counts with 3 existing users.
2. Write a function record_login(user_dict, username) that:
- Checks if the user exists.
- If they exist, increment their count by 1.
- If they are new, add them to the dictionary with a count of 1 using .setdefault() or a standard assignment.
3. Update the dictionary with a batch of new users using .update().

login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}
"""
print("Problem 1 Solution:")
login_counts = {"admin": 5, "dev_user": 12, "guest_1": 1}

def record_login(user_dict, username):
    if username in user_dict:
        user_dict[username] += 1
    else:
        user_dict.setdefault(username, 1)
        #user_dict[username]= 1
    return user_dict

record_login(login_counts, "admin") # check login for existing user
record_login(login_counts, "support_user") # check login for new user
print(f"login_counts after attempted logins: {login_counts}")

new_logins = {"guest_2": 1, "dev_user_2": 1, "new_user": 1}
login_counts.update(new_logins)
print(f"Updated login_counts : {login_counts}")


"""
Problem 2: The "Menu Optimizer" (Deletion & Extraction)
The Scenario: You are managing a digital cafe menu. The dictionary contains item_name: price.
The Task:Given a dictionary of 5 items, 
- use a for loop and .items() to print the menu in a clean format.
- The cafe is removing items that cost more than $10.
- Use a loop to find those expensive items and remove them using the del keyword or .pop()                         
menu = { "Espresso": 3.50, "Latte": 4.50, "Gold_Flake_Coffee": 50.00, "Sandwich": 8.00, "Luxury_Truffle": 25.00 }
"""

print("\nProblem 2 Solution:")
menu = { "Espresso": 3.50, "Latte": 4.50, "Gold_Flake_Coffee": 50.00, "Sandwich": 8.00, "Luxury_Truffle": 25.00 }

def print_menu(menu_dict):
    for item, price in menu_dict.items():
        print(f"{item}: ${price}")

print("Original Menu:")
print_menu(menu)
    
# Identifying Expensive Items
expensive_items = [item for item, price in menu.items() if price > 10]

# Delete or removing expensive items
for item in expensive_items:
    del menu[item]
    #menu.pop(item)

print("\nUpdated Menu:")
print_menu(menu)