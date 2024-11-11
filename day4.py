abc = {1:"apple",2:"cherry",3:"banana",4:"straberry",5:"orange"}
print(abc)
print(abc[1])
print(abc[2])
print(abc[5])

x = eval("10+20+30")
print(x)


# Create the dictionary
student = {"name": "John", "age": 21, "grade": "A"}

# Access and print the value of "name"
print(student["name"])

# Given dictionary
car = {"brand": "Toyota", "year": 2020}

# Update the "year" and add "color"
car["year"] = 2023
car["color"] = "red"

# Print the updated dictionary
print(car)

# Given dictionary
prices = {"apple": 0.40, "banana": 0.25, "orange": 0.30}

# Loop through dictionary and print each fruit and its price
for fruit, price in prices.items():
    print(f"{fruit} costs {price}")

# Given dictionary
books = {"Python": "Beginner", "Java": "Intermediate", "C++": "Advanced"}

# Check if "Java" is a key and remove it if found
if "Java" in books:
    del books["Java"]

# Print the final dictionary
print(books)

