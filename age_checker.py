# This is an example of if/elif/else conditions

age = int(input("How old are you? "))

if age < 18:
    print ("Your young")
elif age >= 18 and age <= 30:
    print ("Your still pretty young")
elif age >=30 and age <= 50:
    print ("Hmm not so young are we")
elif age >= 50 and age < 100:
    print("Old?")
elif age == 100:
    print("Safe to say you're old!")
else:
    print("Can't even comprehend that age, sorry!")
    