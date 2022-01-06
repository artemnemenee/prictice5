def f(name):
    name = name.split(' ')
    return (name[0][0] + '.' + name[1][0] + '.' + name [2][0] + '.')
p = input("Введите полные ФИО:")
print(f(p))
