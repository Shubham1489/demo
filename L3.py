# Function to find the largest element in a list
def find_largest(lst):
    largest = lst[0]
    for element in lst:
        if element > largest:
            largest = element
    return largest

# Example usage
my_list = input("Enter a list of values separated by spaces: ").split()
print("Largest element:", find_largest(my_list))
