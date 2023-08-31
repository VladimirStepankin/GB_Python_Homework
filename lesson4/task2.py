# Задача 2.


def key_to_value(**kwargs):
    my_dict = {}
    for key, value in kwargs.items():
        try:
            my_dict[value] = key
        except TypeError:
            my_dict[str(value)] = key
    return my_dict


print(key_to_value(name='Vladimir', profession='student', age=37, city='Moscow', hobbies=['hockey', 'football']))
