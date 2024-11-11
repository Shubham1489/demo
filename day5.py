#1. Write a program to find biggest in 3 numbers using else if
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print(f"The biggest number is: {a}")
elif b >= a and b >= c:
    print(f"The biggest number is: {b}")
else:
    print(f"The biggest number is: {c}")

#2. Write a program to convert number to words
num = int(input("Enter a number (0-9): "))

if num == 0:
    print("Zero")
elif num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
elif num == 5:
    print("Five")
elif num == 6:
    print("Six")
elif num == 7:
    print("Seven")
elif num == 8:
    print("Eight")
elif num == 9:
    print("Nine")
else:
    print("Invalid")

#3. Print 100 on console using For loop
for i in range(1):
    print(100)

#4. WAP to print hello 10 times
for i in range(10):
    print("Hello")

#5. WAP to display numbers from 0 to 12
for i in range(13):
    print(i)

#6. WAP to display odd numbers from 0 to 20
for i in range(1, 21, 2):
    print(i)

#7. WAP to display numbers from 10 to 1 in Descending Order
for i in range(10, 0, -1):
    print(i)

#8. WAP to print sum of numbers present inside list
num = [1, 2, 3, 4, 5]
s = sum(num)
print(f"The sum of the list is: {s}")

#9. WAP to iterate over list using For lop
my_list = ['apple', 'banana', 'cherry']
for item in my_list:
    print(item)

#10. WAP to sum first n numbers using While Loop
n = int(input("Enter a number: "))
s = 0
i = 1

while i <= n:
    s += i
    i += 1

print(f"The sum of the first {n} numbers is: {s}")

#11. WAP to checking condition if number is 11 break the loop and come out of the loop
for i in range(20):
    if i == 11:
        print("Number 11 found, breaking the loop.")
        break
    print(i)
