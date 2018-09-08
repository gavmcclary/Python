# Henry is this what you wanted to do the other day?

# Define a list
lst = ["Eggs","Bread","Milk"]

# Check if your item is in the list using the .index method.
# We know it's in so no need for an else statement here.

if "Bread" in lst:
	print("Bread is in the list at index " +
	          str(lst.index("Bread")))

# Check if another item is in the list.
# This time we know it is not so I have added an else statement.

if "Jam" in lst:
	print("Jam is in the list at index " +
	          str(lst.index("Jam")))
else:
    print("Jam was not in the list")

# Hope that helps. Gav

