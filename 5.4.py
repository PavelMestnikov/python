"""
4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
Подсказка: использовать возможности python, изученные на уроке.
"""
def function_gen(nums):
    for num in nums[1:]:
        if num > nums[nums.index(num)-1]:
            yield num


def function(nums):
    lst = []
    for num in nums[1:]:
        if num > nums[nums.index(num)-1]:
            lst.append(num)
    return lst


src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
func = function_gen(src)
while True:
    try:
        print(next(func))
    except StopIteration:
        break
print(function(src))