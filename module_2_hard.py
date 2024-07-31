number = int(input('Введите число от 3 до 20: '))  # Ввод числа с камня

while number < 3 or number > 20:                    # Проверка валидности числа от 3 до 20
    print('Введено неверное число, повторите ввод')
    number = int(input('Введите число от 3 до 20: '))


def get_password():     # Перебор числа и высчитывание суммы и остатка от деления
    password = []
    for i in range(number):
        if i > 0:
            for j in range(number):
                if j > 0:
                    summ = j + i
                    if summ > number:
                        break
                    elif j == i:
                        continue
                    elif number % summ == 0 and j > i:
                        password += [i, j]
    return password


password = get_password()   # Вызов функции
password = map(str, password)   # Конвертация списка в строку
print('Верный пароль к числу ' + str(number) + ': ' + ''.join(password))
