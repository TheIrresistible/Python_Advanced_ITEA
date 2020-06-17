country = {'Poland': 'Warsaw', 'Greece': 'Athens', 'Germany': 'Berlin', 'Italy': 'Roma'}
list_of_country = ['Poland', 'Ukraine', 'Belarus', 'Romania', 'Greece']

for i in list_of_country:
    for key in country:
        if i == key:
            print(country[key])