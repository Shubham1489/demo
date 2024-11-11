# Function to calculate the sum of all elements in a list
def sum_of_elements(lst):
    total = 0
    for element in lst:
        total += element
    return total

# Example usage
my_list = input("Enter a list of values separated by spaces: ").split()
print("Sum of all elements:", sum_of_elements(my_list))
