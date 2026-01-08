'''
Problem 1: The "Price Tagger"
The Challenge: You are given a list of product prices. You need to write a function that takes this list and a "Discount Percentage." Inside the function, use a list comprehension to create a new list where each price is reduced by that percentage.

prices = [100, 250, 400, 50]
'''
prices = [100, 250, 400, 50]

def dicount_prices(prices, discount):    
    # return computed list using list comprehension to apply discount to each price
    return [price - (price * (discount / 100)) for price in prices ] 

discount = float(input("Enter discount percentage (0-100): "))
#discount = discount/100 if 0 <= discount <= 100 else 0
discounted_prices = dicount_prices(prices, discount)
print(discounted_prices)


'''Problem 2: The "Short Word" Filter
The Challenge: You have a list of words. Some are long, some are short.Create a Lambda function that checks if a word has more than 3 letters (returns True or False).
Use a List Comprehension and that Lambda to create a new list containing only the "Long Words."
'''
words = ["hi", "python", "is", "cool", "code", "a"]

is_long = lambda word: len(word) > 3

long_words = [lword for lword in words if is_long(lword)]

print('Long words: ', long_words)