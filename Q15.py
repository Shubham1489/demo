# Program to print all prime numbers in an interval of 1-10
for num in range(1, 11):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num)
