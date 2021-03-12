"""
Задание 4. Модуль utils
Написать свой модуль utils и перенести в него функцию get_currency_rate() из предыдущего задания (второго или третьего).
Создать скрипт (task4.py), в котором импортировать этот модуль и выполнить вызовы
функции get_currency_rate() для доллара и евро. Результат вывести на экран в виде:

если используется функция из 2-го задания:
USD 75.18
EUR 80.35
либо, если используется функция из 3-го задания
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
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

