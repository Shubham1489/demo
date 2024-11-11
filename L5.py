def duplicates(lst):
    dup = {}
    for element in lst:
        if element in dup:
            dup[element] += 1
        else:
            dup[element] = 1
    # Filter out elements that appear only once
    return {num: count for num, count in dup.items() if count > 1}

# Example usage
my_list = input("Enter a list of values separated by spaces: ").split()
dupli = duplicates(my_list)

# Print result
if dupli:
    print("Duplicates found:")
    for num, count in dupli.items():
        print(f"Number {num} appears {count} times")
else:
    print("No duplicates found")
