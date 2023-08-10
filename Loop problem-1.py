#take an input from the user and print it's multiplication table.
print("Please, input the number:")
number = int(input())

count = 1

while count <= 10:
    print(number, 'x', count, '=', number * count)
    count += 1