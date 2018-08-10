# Examples of Python lists

# A list is defined using the [] (Square) brackets.
# Individual items are seperated by commas.

my_shopping_list = ["Apples","Oranges","Milk", "Bread"]

print("="*20)
print("The list: ")
print("="*20)
print(my_shopping_list)

raw_input("\nPress Enter to advance...")

# We can add items to the list using the .append method
my_shopping_list.append("Butter")

print("="*20)
print("Added Butter: ")
print("="*20)
print(my_shopping_list)

# And we can remove items too - defaults to last item in list.
my_shopping_list.pop()

raw_input("\nPress Enter to advance...")

print("="*20)
print("Removed Butter: ")
print("="*20)
print(my_shopping_list)

# Let's sort the items into alphabetical order
my_shopping_list.sort()

raw_input("\nPress Enter to advance...")

print("="*20)
print("Sorted the list: ")
print("="*20)
print(my_shopping_list)



