def f():
    j = []
    g = 0
    h = 0
    s = 0
    for h in range(3):
        print()
        a = []
        for g in range(3):
            s = input()
            if not 1<=int(s)<=9:
                print('Вы ввели неправильное значение, программа за себя не отвечает')
                break
            a.append(s)
        j.append(a)
    return j
a = f()
print(a)
def V(a):
    p = 0
    q = 0
    x = 0
    i = 0
    ggwp = 0
    for p in range(0,3):
            q += int(a[p][p])
    for p in range(0,3):
            x += int(a[2-p][2-p])
    if q == x:
        for p in range(0,3):
            q = 0
            for i in range(0,3):
                q += int(a[p][i])
            if q != x:
                ggwp = 1
        for p in range(0,3):
            q = 0
            for i in range(0,3):
                    q += int(a[i][p])
            if q != x:
                ggwp = 1
    if ggwp == 1:
        print('Квадрат не магический')
    else: print('Квадрат магический')
    
V(a)

