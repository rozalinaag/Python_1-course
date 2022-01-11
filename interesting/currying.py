"""
Функции высшего порядка - функции, которые принимают в аргументе другие функции или возвращают другие функции.
Карринг — это преобразование функции от многих аргументов в набор функций, каждая из которых является функцией от одного аргумента.
Мы можем передать часть аргументов в функцию и получить обратно функцию, ожидающую остальные аргументы.

"""


def greet_curried(greeting):
    def greet(name):
        print(greeting + ', ' + name)
    return greet

greet_hello = greet_curried('Hello')

greet_hello('German')
greet_hello('Ivan')

# или напрямую greet_curried
greet_curried('Hi')('Roma')

#results:
#Hello, German
#Hello, Ivan
#Hi, Roma
