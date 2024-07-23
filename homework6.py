# Словари
my_dict = {'Alex': 1990, 'Maria': 1996}
print('Dict:', my_dict)
print('Existing value:', my_dict['Alex'])
print('Not existing value:', my_dict.get('All'))
my_dict.update({'Natasha': 1989, 'Andrey': 1990})
Name = my_dict.pop('Maria')
print('Deleted value:', Name)
print('Modified dictionary:', my_dict)

# Множества
my_set = {1, 1, 'Яблоко', 'Яблоко', 42.314, True, 42.314}
print('Set:', my_set)
my_set.add(13)
my_set.add((14, 5))
my_set.discard(42.314)
print('Modified set:', my_set)