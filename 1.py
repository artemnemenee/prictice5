def f(a, b):
    g = 0
    for i in range(0, len(a)):
        if int(b) < int(a[i]):
            print(a[i], end=" ")
        else: g += 1
    if g > 0:
        print('Ничего')
a = list(input('Введите числа списка через запятую:').split(','))
b = input('Введите число:')
f(a, b)
