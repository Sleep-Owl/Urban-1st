# Выполнение задачи с помощью рекурсии
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif len(str_number) <= 1:
        return first

result = get_multiplied_digits(40203)
print(result)

# Выполнение задачи с помощью цикла
def get_multiplied_digits1(number):
    summ = 1
    str_number = str(number)
    for i in str_number:
        if i == '0':
            continue
        else:
            i = int(i)
            summ = i * summ
    return summ

result1 = get_multiplied_digits1(40203)
print(result1)