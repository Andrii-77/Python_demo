# 1)написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
# - перший записує в список нову справу
# - другий повертає всі записи
from email.utils import decode_rfc2231


def notebook():
    todo_list = []

    def add_todo(todo):
        nonlocal todo_list
        todo_list.append(todo)

    def get_all():
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()
# print(get_all())
add_todo('football')
print(get_all())
add_todo('tea')
print(get_all())

# 2) протипізувати перше завдання

from typing import List, Callable


def notebook() -> List[Callable[[str], None] | list[str]]:
    todo_list: list[str] = []

    def add_todo(todo: str) -> None:
        nonlocal todo_list
        todo_list.append(todo)

    def get_all() -> list[str]:
        return todo_list

    return [add_todo, get_all]


add_todo, get_all = notebook()
add_todo('football')
add_todo('tea')
add_todo('golf')
print(get_all())


# 3) створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#
# Приклад:
#
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    num_in_str = str(num)
    arr = []
    for i in range(len(num_in_str)):
        number = num_in_str[i]
        if number != "0":
            arr.append(number + '0' * (len(num_in_str) - i - 1))
    # print(arr)
    result = '+'.join(arr)
    print(result)
    return result

# Якщо не знати join, то можна це прописати трохи інакше:
#     result = ""
#     for i in arr:
#         if result:
#             result += "+" + i
#         else:
#             result = i
#     print(result)

expanded_form(12)
expanded_form(42)
expanded_form(70304)


# 4) створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована цим декоратором,
# та буде виводити це значення після виконання функцій

def decor(func):
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        print('count: ', counter)
        func()
    return inner


@decor
def func1():
    print('func1')


@decor
def func2():
    print('func2')


func1()
func1()
func2()
func1()
