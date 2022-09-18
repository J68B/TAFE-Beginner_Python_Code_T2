### Python Activity Week 1-Algorithms

''' Write a Python script to do the following
Set the price of chocolate bars to be $1.50 in a variable
Tell the user how much chocolate bars are
Ask the user how many bars they want

Calculate the total price of the chocolate bars

Apply a discount of 10% if they buy 20 or more

Tell user the final price of that many bars, e.g.

The price for 25 bars is $33.75 '''

# Set the price of chocolate bars to be $1.50 in a variable
chocBar=1.50

# Tell the user how much chocolate bars are
print("Our delicious chocolate bars are $1.50 each, or there is 10% discount if you buy 20 or more")

# Ask the user how many bars they want
order=int(input("How many chocolate bars would you like to order ? "))
order={:2f}(order)
# totalOrder = "{:.2f}".format(totalOrder)

# Calculate the total price of the chocolate bars
if order > 20:
    print("The total for", order, "bars is ", "$", order * 1.35)
else:
    print("The total for", order, "bars is ", "$", order * 1.50))