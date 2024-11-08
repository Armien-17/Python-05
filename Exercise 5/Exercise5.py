# Question 1: Creating and Modifying Lists

# TODO: Create a list of fruits
fruitlist = ["Apple", "Pear", "Pineapple", "Watermelon", "Sweet Melon"]
print (fruitlist)
# TODO: Add a fruit to the end of the list
fruitlist.append("Mango")
# TODO: Insert a fruit at the beginning of the list
fruitlist.insert(0, "Strawberry")
# TODO: Remove a fruit from the list
fruitlist.remove("Pear")
# TODO: Print the modified list
print(fruitlist)

#-------------------------------------------------------------------------
# Question 2: List Operations

# TODO: Create a list of numbers from 1 to 5
numberlist = [1, 2, 3, 4, 5]
# TODO: Create a new list with each number squared
squared_numberlist = [num**2 for num in numberlist]
# TODO: Find the sum and average of the original numbers
Total_sum = sum(numberlist)
average = Total_sum / len(numberlist)
# TODO: Print the results
print("orignal number :",numberlist)
print("squared number:",squared_numberlist)
print("sum of original number:",Total_sum)
print("average of original number:",average)

#-------------------------------------------------------------------------
# Question 3: Creating and Modifying Dictionaries

# TODO: Create a dictionary of countries and their capitals
countries = {
    "South Africa": "Cape Town",
    "America": "Washington,D.C",
    "Mexico": "Mexico City",
    "Columbia": "Bogata"
}
# TODO: Add a new country-capital pair
countries["Egypt"] = "Cairo"
# TODO: Update the capital of an existing country
countries.update({"South Africa": "Joburg"})
# TODO: Remove a country-capital pair
countries.pop("Columbia")
# TODO: Print the modified dictionary
print(countries)
#-------------------------------------------------------------------------
# Question 4: Dictionary Operations

# TODO: Create a dictionary of fruit colors
fruit_colors = {
    "Grape": "Green",
    "Litchi": "Brown",
    "Plum": "Purple",
    "Pineapple": "Yellow"
    }
# TODO: Print all the fruits (keys)
print(list(fruit_colors.keys()))
# TODO: Print all the colors (values)
print(list(fruit_colors.values()))
# TODO: Print each fruit and its color
print(fruit_colors)
# TODO: Check if a fruit is in the dictionary and print its color
fruit_to_check = "Plum"

if fruit_to_check in fruit_colors:
    print(f"The color of {fruit_to_check} is {fruit_colors[fruit_to_check]}")
else:
    print(f"{fruit_to_check}is not in the dictionary.")