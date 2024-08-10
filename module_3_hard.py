data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


def calculate_structure_sum(x, *args, a=0, **kwargs):
    sum_ = 0
    for list_summ in data_structure[0]:
        sum_ += int(list_summ)

    dict_ = data_structure[1]
    for key, values in dict_.items():
        sum_ += len(key) + values

    tuple_ = data_structure[2]
    tuple_dict_ = tuple_[1]
    sum_ += tuple_[0]
    for key, values in tuple_dict_.items():
        sum_ += len(key) + values

    sum_ += len(data_structure[3])

    tuple2_ = data_structure[4]
    list_of_tuple = list(*tuple2_[1])
    tuple2_of_list = tuple(*list_of_tuple)
    tuple3_of_list = tuple2_of_list[2]
    sum_ += tuple2_of_list[0] + len(tuple2_of_list[1])
    sum_ += len(tuple3_of_list[0]) + tuple3_of_list[1]

    return sum_


result = calculate_structure_sum(data_structure)
print(result)
