"""
Задание 2. Курс Валюты
Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
Код валюты может быть в произвольном регистре.
Функция должна возвращать результат числового типа, например float.
Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
http://www.cbr.ru/scripts/XML_daily.asp.

Выведите на экран курсы для доллара и евро, используя написанную функцию.

Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
"""

import requests

def get_currency_rate(valute, money = 1):
    r = requests.get("http://www.cbr.ru/scripts/XML_daily.asp")
    data = r.content.decode("windows-1251")
    lst1 = []
    lst2 = []
    for i in range(len(data)):
        try:
            if data[i: i+10] == "<CharCode>":
                lst1.append(data[i+10: i+13])
            if data[i: i+7] == "<Value>":
                num = ""
                for digit in data[i+7: i+14]:
                    if digit == ",":
                        num += "."
                    else:
                        num += digit
                lst2.append(float(num))
        except IndexError:
            continue
    dct = {}
    for key, value in zip(lst1, lst2):
        dct[key] = value
    try:
        return dct[valute] * money
    except KeyError:
        return None

while True:
    a, b = map(str, input().split())
    b = int(b)
    print(get_currency_rate(a, b))