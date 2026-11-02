# SELF-ASSESSMENT

# 1. The first bug I spotted was the sales bug because when I opened the file in Visual Studio Code, there was a red line that made the error more obvious.
#  The other bugs were harder to find, so I had to use print() statements inside the loop to see what was happening. 
# I also explained the code out loud to my tiny captain duck and used AI to check my understanding. This shows that I am starting to understand how to debug by looking at errors, testing the code, and explaining what the code is doing instead of just guessing.

# 2. The apply_discount(price, tier) function takes the original price and the customer's discount tier as inputs. 
# It checks whether the customer is gold, silver, or bronze and applies a 15%, 10%, or 5% discount.
# If the customer does not have one of these tiers, the price stays the same. 
# The function returns the discounted price. 
# A colleague could use this function without reading the body because the function name and parameters explain what information it needs and what it does.

# 3. I used AI for Exercise 5 after explaining each error in my own words to my rubber captain duck. 
# I used AI to check my understanding and help me confirm my solutions instead of just copying the answers. 
# I also used AI for Exercise 2 because I was unsure how to organize the if, elif, and else statements for the different discount tiers.
#  For Exercise 3, I used the functions from Exercise 2 and Exercise 1 together to calculate the final price after applying a discount and adding tax. 
# AI helped me understand how to organize the functions and use them together. 
# Overall, I think using AI helped build my understanding because I tried to solve the problems myself first and then used AI to check and improve my understanding of actually writing the code. 

# Exercise 1

# Defining a funtion 
def calculate_tax(price, rate):
    return price * rate

# Calling the funtion 

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7% ${tax1:.2f}")
print(f"Tax for $250 at 8% ${tax2:.2f}")

# Exercise 2

# Defining a funtion with multipal parameters
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "sliver": 
        return price* 0.90
    elif tier == "bronze":
        return price * 0.95
    else: 
        return price

# Calling the funtion with diffenren tiers 
original_price = 200

print(f"gold:   ${apply_discount(original_price, 'gold'):.2f}")
print(f"silver: ${apply_discount(original_price, 'silver'):.2f}")
print(f"bronze: ${apply_discount(original_price, 'bronze'):.2f}")
print(f"none:   ${apply_discount(original_price, 'none'):.2f}")

# Exercise 3

# Use both functions together
discounted = apply_discount(200, "gold")
with_tax = discounted + calculate_tax(discounted, 0.07)
print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${with_tax:.2f}")


# Third function that calls both
def final_price(price, tier, tax_rate):
    discounted_price = apply_discount(price, tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax


print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')


# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]
for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price} | Tier: {tier} | Final: ${total:.2f}")


# Exercise 5 

# broken_sales.py - trace and diagnose before fixing anything.
# sales = [120, 80, 250, 175, 90]
 
# Bug 1: total = sale replaced total on every pass, so it ended up as just the last sale (90). The program printed Total: $90 instead of $715 but when I add 
# print(total) inside the loop and saw it go 120, 80, 250, 175, 90. That showed me total = sale replaces the total each time instead of adding to it.
# AI Explainer: This bug has no error message, so there was nothing to paste.  It is a logic error.
# My fix: I changed total = sale to total += sale so each sale is added to the running total instead of replacing it. The total is now $715.

# total = 0
# for sale in sales:
#     total += sale
# print(f"Total: ${total}")
 
# Bug 2: the for line was missing its colon, which is a SyntaxError.Python refused to run the file and pointed at the line. When I read the line"for sale in sales" to my rubber duck
# (which in this case for me was an tiny captain duck on my desk) I noticed it was the only loop line that did not end in a colon.
# AI Explainer: I pasted only "SyntaxError: expected ':'". The AI explained the for line is missing a colon at the end, which causes a SyntaxError. Python requires a colon after the loop header.
# My fix: I added the missing : to the end of the for line.

# count = 0
# for sale in sales:
#     count += 1
# print(f"Count: {count}")
 
# Bug 3: The list has 5 items, so the indexes go from 0 to 4. The condition i <= len(sales) allows i to reach 5, but index 5 does not exist. 
# This causes an IndexError because Python tries to access an item that is not in the list.
# AI Explainer: I pasted print(sales[i]) IndexError: list index out of range into AI. The AI explained 
# the bug is <= in the loop condition. List indexes run from 0 to len(sales) - 1, so when i equals len(sales), sales[i] goes one past the end and raises IndexError.
# My fix: I changed while i <= len(sales) to while i < len(sales) so the loop stops when i is 5 and never reads an index that does not exist.

# while i < len(sales):
#     print(sales[i])
#     i += 1


# Exercise 6
# Explaning the Scope: x outside the function is global. Inside double_it(), the assignment x = 999 creates a new local variable that exists only while the function runs and it does not change the global x.

x = 100  # global variable


def double_it():
    x = 999  # local variable, different from global x
    return x * 2


print(x)            # 100  (global)
print(double_it())  # 1998 (uses local x = 999)
print(x)            # 100  (global x never changed)

