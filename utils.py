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

