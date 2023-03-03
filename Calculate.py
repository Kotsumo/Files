import operator

settings = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow,
    '%': operator.mod,
    '//': operator.floordiv
}

a = int(input("Введите первое значение"))
b = int(input("Введите второе значение"))
c = input("Введите математическую операцию: +, -, /, *")
result = settings[c](a, b)
print(result)