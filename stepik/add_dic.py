"""
Если ключ keykey есть в словаре dd, то добавьте значение valuevalue в список, который хранится по этому ключу.
Если ключа keykey нет в словаре, то нужно добавить значение в список по ключу 2 * key2. Если и ключа 2 * key2 нет,
то нужно добавить ключ 2 * key2 в словарь и сопоставить ему список из переданного элемента [value]."""


def update_dictionary(d, key, value):
    if key in d:
        d[key] += [value]
    elif 2 * key in d:
        d[2 * key] += [value]
    else:
        d[2 * key] = [value]
        
"""def update_dictionary(d, key, value):
    if (d.get(key)==None):
        if d.get(2*key)==None:
            d[2*key] = [value]
        else:
            d[2*key].append(value)
    else:
        d[key].append(value)"""
