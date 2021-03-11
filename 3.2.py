"""
2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу с числительными,
начинающимися с заглавной буквы. Например:
>>> >>> num_translate_adv("One")
"Один"
>>> num_translate_adv("two")
"два"
"""



def num_translate_adv(num):
    highletters = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(1040, 1072)]

    if num[0] in highletters:
        upper = True
    else:
        upper = False
    num = num.lower()

    numbers = {"один":"one", "два":"two", "три":"three", "четыре":"four", "пять":"five",
              "шесть":"six", "семь":"seven", "восемь":"eight", "девять":"nine", "десять":"ten"}

    if num in numbers:
        translated_num = numbers[num]
    else:
        try:
            translated_num = list(numbers.keys())[list(numbers.values()).index(num)]
        except ValueError:
            return None

    if upper == True:
        return translated_num[0].upper() + translated_num[1:]
    else:
        return translated_num

while True:
    print(num_translate_adv(str(input())))