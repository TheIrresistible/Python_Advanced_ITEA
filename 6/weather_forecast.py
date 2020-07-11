import bs4
import requests
import datetime


def get_weather(p):
    return p[0].getText()


city = input('Введіть місто: ').replace(' ', '-')
try:
    day, month, year = [str(x) for x in input("Введіть дату: ").split('.')]
except ValueError:
    print('Некоректно введена дата (д.м.р)')
    exit()

s = requests.get(f'https://ua.sinoptik.ua/погода-{city}/{year}-{month}-{day}')
b = bs4.BeautifulSoup(s.text, "html.parser")
p1 = b.select('.temperature .p3')
p2 = b.select('.temperature .p4')
p3 = b.select('.temperature .p5')
p4 = b.select('.temperature .p6')
today = datetime.date.today()

print(f'Погода в місті {city.capitalize()} за {day}.{month}.{year}')
try:
    if today.year <= int(year) and today.month <= int(month) and today.day + 1 < int(day):
        print(f'Максимальна: {get_weather(p1)}')
        print(f'Мнімальна: {get_weather(p2)}')
    else:
        print(f'Ранок: {get_weather(p1)} {get_weather(p2)}')
        print(f'День: {get_weather(p3)} {get_weather(p4)}')
        p = b.select('.rSide .description')
        print(get_weather(p).strip())
except IndexError:
    print('Некоректно введені дані або немає даних за цей день')
