# Reflection Questions
# 1. The most surprising thing about Python lists is that they are mutable and
#    flexible: you can add, remove, and sort items in place, and methods like
#    .sort() and .append() change the original list instead of returning a new
#    one. I also didn't expect negative indices like [-1] to be so handy.
#
# 2. In an internship, I might have had to track daily sales or customer orders
#    in Excel and copy formulas down for every new row. With a Python list, I
#    could loop over all the numbers once to filter, discount, or average them
#    in a few lines, and rerun the same code whenever new data came in, saving
#    time and avoiding copy-paste mistakes.
 
# Exercise 1: Build the list
print("----Exercise 1: Build the list----")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
 
#Exercise 2: Index Pratice

print("----Exercise 2: Index Pratice----")
print(inventory[0]) #always grabs the first item 
print(inventory[-1]) #always grabs the last item 

middle = len(inventory) // 2
print(inventory[middle]) #grabs the middle item (not hard coded)

#Excercise 3
print("----Exercise 3: List Slicing----")
print(inventory[:3])   # first three items
print(inventory[-2:])  # last two items
print(inventory[::2])  # every other item

#Excercise 4
print("----Exercise 4: Modify----")

print(inventory)
 
inventory.append("envelope")
print("After append:", inventory)
 
inventory.remove("tape")
print("After remove:", inventory)
 
inventory.sort()
print("After sort:", inventory)

#Excercise 5
print("----Exercise 5: Tuple Comparison----")

coords = (40.7128, -74.0060)  # NYC
 
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples are useful for coordinates because they are immutable, "
          "so a location can't be changed by accident.")
 
print(coords)

#Exercise 6
print("----Exercise 6: List Average Sales-----")

sales = [100, 250, 75, 480, 200]
 
total = sum(sales)
count = len(sales)
average = total / count
 
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")



# Bonus: finding best and worst manually with a loop
best = sales[0]
worst = sales[0]

for amount in sales:
    if amount > best:
        best = amount
    if amount < worst:
        worst = amount

print(f"Best sale (loop): {best}")
print(f"Worst sale (loop): {worst}")


#Exercise 7
print("----Excercsie 7: Accumulator pattern---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
 
discounted = []  # an empty list
for price in prices:
    discounted.append(round(price * 0.9, 2))
 
print("Original:  ", prices)
print("Discounted:", discounted)

#Exercise 8
print("----Exercise 8: Filter----")

sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
 
high_sales = []  # an empty list
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
 
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")
