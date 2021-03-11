"""
3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
Например:
>>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
{
    "И": ["Иван", "Илья"],
    "М": ["Мария"], "П": ["Петр"]
}
"""

"""
def thesaurus_adv(lst):
    dct = {}
    for name in lst:
        first_letter = name[0]
        if first_letter in dct:
            dct[first_letter].append(name)
        else:
            dct[first_letter] = [name]
    return dct


print(thesaurus_adv(["Иван", "Мария", "Марина", "Петр", "Павел", "Илья", "Марат"]))
"""


def thesaurus_adv(lst):
    dct = {}
    for name in lst:
        first_letter_surname = ""
        first_letter_name = name[0]
        for i in range(len(name)):
            if name[i] == " ":
                first_letter_surname = name[i + 1]
                break
        if first_letter_surname not in dct:
            dct[first_letter_surname] = [{first_letter_name: [name]}]
        else:
            if first_letter_name in dct[first_letter_surname][0]:
                dct[first_letter_surname][0][first_letter_name].append(name)
            else:
                dct[first_letter_surname].append({first_letter_name: [name]})
    return dct


names = thesaurus_adv(["Иван Петров", "Мария Иванова", "Марина Сидорова", "Петр Наумов",
                       "Павел Местников", "Паша Местников", "Илья Нестеров", "Марат Местников"])
for keys, values in names.items():
    print(keys)
    print(values)