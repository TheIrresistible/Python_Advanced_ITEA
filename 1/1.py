n = int(input('Input N: '))

list_of_number = range(0, n, 1)

for i in list_of_number:
    if i % 2 == 0:
        print(i)
