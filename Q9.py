import cmath  # For complex numbers

a = int(input("x : "))
b = int(input("b : "))
c = int(input("c : "))

d = (b ** 2) - (4 * a * c)

# Find two solutions
s1 = (-b + cmath.sqrt(d)) / (2 * a)
s2 = (-b - cmath.sqrt(d)) / (2 * a)

print(f"The solutions are {s1} and {s2}")
