immutable_var = (['Список'], 'Переменная неизменная', 533, True)
print(immutable_var)
immutable_var[0][0] = '1'
print(immutable_var)
mutable_list = ['Переменная изменяемая', 533, True]
print(mutable_list)
mutable_list[0] = 1
print(mutable_list)