# Function to reverse a list without using built-in functions
def reverse_list(lst):
    reversed_list = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_list.append(lst[i])
    return reversed_list

# Example usage
my_list = input("Enter a list of values separated by spaces: ").split()
print("Reversed list:", reverse_list(my_list))
