def f():
    s = 0
    a = []
    g = True
    print("Вводите числа списка поочередно:")
    while ...:
        s = input()
        if not s:
            break
        a.append(s)
    n = int(input('Введите число n: '))
    for i in range(0,len(a)):
        if n < int(a[i]):
            print(a[i])
            g = None
    if g:
        print('Таких чисел нет')
f() 