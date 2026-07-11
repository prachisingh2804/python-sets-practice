# ==============================
# Python Sets - Basic Concepts
# Author: Prachi Singh
# ==============================

# Creating a Set
fruits = {"Apple", "Banana", "Mango"}
print("Original Set:", fruits)

# add()
fruits.add("Orange")
print("After add():", fruits)

# remove()
fruits.remove("Apple")
print("After remove():", fruits)

# discard()
fruits.discard("Pineapple")   # No error if element doesn't exist
print("After discard():", fruits)

# len()
print("Total Elements:", len(fruits))

# clear()
temp = {"Red", "Blue"}
temp.clear()
print("After clear():", temp)
