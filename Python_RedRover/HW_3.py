line_0 = "----------------"
line = line_0 * 9
print(line)

# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
print("3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3")

my_list = ['a', 'b', [1, 2, 3], 'd']
print("my_list[2] =", my_list[2])
print()
print(line)

# 3.2. Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
print("3.2. Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100] "
      "- получите сумму всех чисел, "
      "- распечатайте все строки, где есть буква 'a'")

list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]

list_2 = []
for i in list_1:
    if isinstance(i, int):
        list_2.append(i)
print("получите сумму всех чисел= ", sum(list_2))

list_3 = []
for i in list_1:
    if type(i) == int:
        list_3.append(i)
print("получите сумму всех чисел= ", sum(list_3))


# "Строки, где есть буква 'a'
list_4 = []
for i in list_1:
    if isinstance(i, str) and 'a' in i:
        list_4.append(i)
print("Строки, где есть буква 'a' =", list_4)
print()
print(line)

# 3.3.  Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж
print("3.3. Превратите лист ['cat', 'dog', 'horse', 'cow'] в кортеж")

lst = ['cat', 'dog', 'horse', 'cow']
lst_1 = tuple(lst)
print("Кортеж (tuple) lst_1 =", type(lst_1))
print("tuple(lst) =", lst_1)
print()
print(line)

# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')

print("3.4. Напишите программу, которая определяет, какая семья больше. ")
print("1) Программа имеет два input() - например, family_1, family_2. ")
print("2) Членов семьи нужно перечислить через запятую. ")
print("Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print('Equal')")

# family_1 = input()
# family_2 = input()
family_1 = "Андрей, Ирина"
family_2 = "Антон, Саша, Катя"

members_family_1 = family_1.split(',')
members_family_2 = family_2.split(',')

if len(members_family_1) > len(members_family_2):
    print(family_1)
elif len(members_family_2) > len(members_family_1):
    print(family_2)
else:
    print("Equal")
print()
print(line)

# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

print("3.5 Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию \n"
      "о вашем любимом фильме. \n"
      "  - распечатайте только ключи\n"
      "  - распечатайте только значения\n"
      "  - распечатайте пары ключ - значение\n")

film = {
    "title": "The Shawshank Redemption",
    "director": "Frank Darabont",
    "year": 1994,
    "budget": 25000000,
    "main_actor": "Tim Robbins",
    "slogan": "Fear can hold you prisoner. Hope can set you free."
}

# Вывод информации о фильме
print("Title:", film["title"])
print("Director:", film["director"])
print("Year:", film["year"])
print("Budget:", film["budget"])
print("Main Actor:", film["main_actor"])
print("Slogan:", film["slogan"])

print()
print(line)

# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
print("3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}")

my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}

print("sum(my_dictionary.values()) =", sum(my_dictionary.values()))
print()
print(line)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
print("3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]")

list_1 = [1, 2, 3, 4, 5, 3, 2, 1]
# Преобразуем список во множество, чтобы удалить дубликаты
unique_set = set(list_1)

# Преобразуем множество обратно в список
unique_list = list(unique_set)
print(unique_list)
print()
print(line)


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга

print("3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785} \n"
      "     - найдите значения, которые встречаются в обоих множествах \n"
      "     - найдите значения, которые не встречаются в обоих множествах \n"
      "     - проверьте являются ли эти множества подмножествами друг друга \n")

set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}

# Значения, которые встречаются в обоих множествах
intersec = set1.intersection(set2)
print("Значения, которые встречаются в обоих множествах:", intersec)

# Значения, которые не встречаются в обоих множествах
symmetricdiffer = set1.symmetric_difference(set2)
print("Значения, которые не встречаются в обоих множествах:", symmetricdiffer)

# Являются ли множества подмножествами друг друга
is_subset1 = set1.issubset(set2)
is_subset2 = set2.issubset(set1)
print("Множество set1 является подмножеством set2:", is_subset1)
print("Множество set2 является подмножеством set1:", is_subset2)