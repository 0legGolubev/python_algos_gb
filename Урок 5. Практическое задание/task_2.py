"""
2.*	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого – это цифры
шестнадцатеричного числа. Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел: [‘C’, ‘F’, ‘1’], произведение: [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию
из модуля collections. Для лучшее освоения материала можете даже сделать
несколько решений этого задания, применив несколько коллекций
из модуля collections. Также попробуйте решить задачу вообще без collections
и применить только ваши знания по ООП. (в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
"""

from collections import defaultdict
from functools import reduce


def calc():
    nums = defaultdict(list)

    # defaultdict(<class 'list'>, {'1-A2': ['A', '2'], '2-C4F': ['C', '4',
    # 'F']})
    for d in range(2):
        n = input(f"Введите {d + 1}-е натуральное шестнадцатиричное число: ")
        nums[f"{d + 1}-{n}"] = list(n)
    print(nums)
    # defaultdict(<class 'list'>, {'1-A2': ['A', '2'], '2-C4F': ['C', '4',
    # 'F']}

    # 16-указываем с числами какой системы делаем операции
    summ = sum([int(''.join(i), 16) for i in nums.values()])
    print(summ)
    # '%X'	Число в шестнадцатеричной системе счисления

    print("Сумма: ", list('%X' % summ))

    mult = reduce(lambda a, b: a * b,
                  [int(''.join(i), 16) for i in nums.values()])
    print("Произведение: ", list('%X' % mult))


calc()
