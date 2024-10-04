first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(a) - len(b) for a, b in zip(first, second) if len(a) != len(b))


def compare_lengths(first_list, second_list):
    result = []
    for i in range(len(first_list)):
        if len(first_list[i]) != len(second_list[i]):
            result.append(False)
        else:
            result.append(True)
    return result


second_result = compare_lengths(first, second)

print(list(first_result))
print(list(second_result))
