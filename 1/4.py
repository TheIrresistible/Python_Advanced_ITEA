def bank(s, y, p):
    for i in range(y):
        s = s * (p / 100) + s
    return s


summ = int(input('Sum: '))
years = int(input('Years: '))
percentege = int(input('Percentege: '))

print(bank(summ, years, percentege))
