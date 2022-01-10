def a(tex):
    count = 0
    for i in tex:
        if gl.find(i) != -1:
            count += 1
    return count

def b(tex):
    count = 0
    for i in tex:
        if sogl.find(i) != -1:
            count += 1
    return count

tex = str(input("Текст: "))
gl = "Аа, Ее, Ёё, Ии, Оо, Уу, Ыы, Ээ, Юю, Яя"
sogl = "Бб, Вв, Гг, Дд, Жж, Зз, Йй, Кк, Лл, Мм, Нн, Пп, Рр, Сс, Тт, Фф, Хх, Чч, Цц, Шш, Щщ"
choice = str(input("согласная(с) или гласная(г): "))
if choice == "с":
    print(b(tex))
elif choice == "г":
    print(a(tex))
