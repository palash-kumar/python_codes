"""
Problem 1: The "Email Validator" (Cleaning & Tuples)
The Scenario: You have a list of raw user inputs. You need to separate the Username from the Domain and return them as a "locked" pair.
The Task: Write a function process_email(email) that:Strips any whitespace.Converts it to lowercase.Splits the string at the @ symbol.Returns the result as a Tuple: (username, domain).
"""

def process_email(email):
    email = email.strip().lower()
    username, domain = email.split('@')
    return (username, domain)

email = "pknath.edu@gmail.com "
print(f"solution 1: {process_email(email)}")

"""
Problem 2: The "Data Masker" (List Comp & Slicing)
The Scenario: You have a list of credit card numbers (strings). For security, you need to hide all numbers except the last 4.
The Task: Use a List Comprehension to take a list of 16-digit strings and turn them into "masked" versions where the first 12 digits are * and the last 4 are visible.
"""
cards = ["1234567812345678", "9876543298765432", "1111222233334444"]

masked_cards = ['*' * 12 + card[-4:] for card in cards]
print(f"\nsolution 2: {masked_cards}")

"""
Problem 3: The "Inventory Analyzer" (Everything Combined)
The Challenge: You are given a list of product strings in this format: "itemName:Price".
Example: ["Laptop:1000", "Mouse:25", "Monitor:300"]
The Task: Write a script that:Uses a List Comprehension to turn that list into a list of Tuples: [("Laptop", 1000), ...]. (Hint: You'll need to split(":") and convert the price to an int).
Uses the max() and min() functions on the prices to find the most expensive and cheapest items.
"""

raw_inventory = ["Laptop:1000", "Mouse:25", "Monitor:300", "Keyboard:50"]

inventory = [(item.split(':')[0], int(item.split(':')[1])) for item in raw_inventory]

print(f"\nsolution 3:")
print(inventory)

most_expensive = max(inventory, key=lambda x: x[1])
cheapest = min(inventory, key=lambda x: x[1])

print(f"Most expensive item: {most_expensive}")
print(f"Cheapest item: {cheapest}")