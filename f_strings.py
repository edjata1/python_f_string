# f string to format strings

# examlpe from previous example

person = "Empress"
coins = 3

print("------- concatenating with +  -------")
# concatenated string 
print("\n" + person + " has " + str(coins) + " coins left.")

print()
print("------- old formatting ways,  %s -------")
# %s way
message = "\n%s has %s coins left" % (person, coins)
print(message)

print()
print("------- newer method, .format method  -------")

# dot format method
message = "\n{} has {} coins left".format(person, coins)
print(message)

# dot format method with index #'s positioning, can flip around
message = "\n{1} has {0} coins left".format(coins, person)
print(message)

# refer to them by name, setting values of parameters
message = "\n{person} has {coins} coins left".format(coins = coins, person = person)
print(message)


# dictionary {}
player = { "person" : "Empress", "coins" : 3}


# pull from dictionary based on key names
message = "\n{person} has {coins} coins left".format(**player)
print(message)

print()
print("----------- f-strings! This is the way ------------")
# f-strings! This is the way

# inserting the values from variables
message = f"{person} has {coins} coins left."
print(message)

print()
print("----------- insert equations ------------")
# inserting equation
message = f"{person} has {2 * 5} coins left."
print(message)

print()
print("----------- insert method ------------")
# inserting methods
message = f"{person.lower()} has {2 *8} coins left."
print(message)

print()
print("----------- insert dictionary ------------")
# inserting dictionary
message = f"{player['person']} has {player['coins']} coins left."
print(message)

print()
print("----------- insert formatting options ------------")
# inserting formatting options 2 decimal fixed
num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2f}\n")

print()
print("----------- insert loops over range ------------")
# inserting in a loop
for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")

print()
print("----------- insert loops division ------------")
# inserting in a loop
for num in range(1, 11):
    print(f"{num} divided by 4.52 is {num / 4.52:.2%}")

print("Note: visit w3 school website ->> Python String format() Method")
txt ="for only {coins:2f} cents."
print(txt.format(coins = 49))

print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")
print("-------   -------")