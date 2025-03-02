# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

st = 'as 23 fdfdg544'
st1 = ''
for i in st:
    if i.isdigit():
        if st1:
            st1 += ','
        st1 += i
print(st1)

# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
#   st = 'as 23 fdfdg544 34' #введена строка
#   23, 544, 34              #вивело в консолі

st = 'as 23 fdfdg544 34'
st1 = ''
number = ''
for i in st:
    if i.isdigit():
        number += i
    else:
        if number:
            if st1:
                st1 += ', '
            st1 += number
            number = ""
if number:
    if st1:
        st1 += ', '
    st1 += number
print(st1)

# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

greeting = 'Hello, world'
list1 = []
for i in greeting:
    list1.append(i.upper())
print(list1)

# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

list2 = []
for i in range(50):
    if i % 2 != 0:
        list2.append(i ** 2)
print(list2)

# function
#
# - створити функцію яка виводить ліст

list3 = ['Hello', 5, 7.7, True]


def forscreen(arr):
    print(arr)


forscreen(list3)


# - створити функцію яка приймає три числа та виводить та повертає найбільше.

def forthreenum(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        max_num = num1
    elif num2 >= num1 and num2 >= num3:
        max_num = num2
    else:
        max_num = num3
    print(max_num)
    return max_num


forthreenum(25, 45, 15)


# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

def formanynum(*args):
    num_max = args[0]
    for i in args:
        if i > num_max:
            num_max = i
    print(num_max)

    num_min = args[0]
    for i in args:
        if i < num_min:
            num_min = i
    # print(num_min)
    return num_min


formanynum(22, 6, 33, -8, 77, 0)

# - створити функцію яка повертає найбільше число з ліста

list4 = [85, -5, 41, 33, 77]


def maxnumfromlist(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    # print(max_num)
    return max_num


maxnumfromlist(list4)


# - створити функцію яка повертає найменьше число з ліста

def minnumfromlist(arr):
    min_num = arr[0]
    for num in arr:
        if num < min_num:
            min_num = num
    # print(min_num)
    return min_num


minnumfromlist(list4)


# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.

def amountnumfromlist(arr):
    amount = 0
    for i in arr:
        amount += i
    # print(amount)
    return amount


amountnumfromlist(list4)


# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.

def avervalfromlist(arr):
    amount = 0
    counter = 0
    for i in arr:
        amount += i
        counter += 1
    # print(amount)
    # print(counter)
    # print(amount / counter)
    return amount / counter

avervalfromlist(list4)


# 1)Дан list:
#   list = [22, 3,5,2,8,2,-23, 8,23,5]
#   - знайти мін число
#   - видалити усі дублікати
#   - замінити кожне 4-те значення на 'X'

list = [22, 3,5,2,8,2,-23, 8,23,5]

min_num=list[0]
for num in list:
   if num<min_num:
       min_num=num
print(min_num)


nodublicatelist=[]
for num in list:
    if num not in nodublicatelist:
        nodublicatelist.append(num)
print(nodublicatelist)


for i in range(3, len(list), 4):
    list[i] = 'X'
print(list)


# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції

def square(side):
    print("*"*side)
    counter = 0
    while counter < side-2:
        print('*', " "*(side-2), '*')
        counter+=1
    print("*" * side)

square(5)


# 3) вывести табличку множення за допомогою цикла while

# def multiplicationtable(numeric):
#     counter = 1
#     multiplier = 1
#     while counter <= 10:
#         print(f"{multiplier} * {numeric} = {numeric*multiplier}" )
#         counter+=1
#         multiplier+=1
#
# multiplicationtable(2)

def multiplicationtable():
    multiplier = 1
    while multiplier <= 10:
        numeric = 1
        while numeric <= 10:
            print(f"{numeric} * {multiplier} = {multiplier*numeric}")

            numeric+=1
        multiplier += 1
        print()
multiplicationtable()

# 4) переробити це завдання під меню

# Не розумію цього завдання. Що таке меню???