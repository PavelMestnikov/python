"""
Задание 5. * Вызов с командной строки
Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли,
а коды валют ему дожны передавать через аргументы командной строки (там может быть один или несколько кодов).
Вывод курсов сделать в том же порядке, что присланные аргументы
Например:

python task5.py USD EUR
USD 75.18, 2020-09-05
EUR 80.35, 2020-09-05
"""

import utils
import sys

argv = sys.argv
for i in range(len(argv)-1):
    print(argv[i+1], "{:.2f}".format(utils.get_currency_rate(argv[i+1], 1)))