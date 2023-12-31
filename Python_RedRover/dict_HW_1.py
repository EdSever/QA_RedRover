# Задание к ревью по словарям:
# 1. Создать словарь my_dict с 3 парами ключ: значение.
# 2. Создать словарь new_dict с 2 парами ключ: значение(отличные от первого словаря)
# 3. Объединить два словаря через распаковку в новый словарь all_dict. Вывести его в терминал.
# 4. Изменить значение любого ключа в all_dict на '0' методом pop. Вывести в терминал изменённый словарь.
# 5. Удалить последнюю пару ключ: значение из словаря all_dict методом popitem.
# 6. Создать список из 3 кортежей в которых по 2 значения.
# 7. Преобразовать этот список в словарь и вывести в терминал значение второго(позиция 1) ключа.

# 1. Создать словарь my_dict с 3 парами ключ: значение.

my_dict = {
    "item_name": "Smartphone",           # Название товара
    "price": 45.50,                      # Цена товара
    "quantity": 2,                       # Количество товара
    "item_id": "XYZ789",                 # Идентификационный номер товара
    "date": "2023-08-21",                # Дата покупки
    "cashier": "Emily Johnson",          # Имя кассира
    "payment_method": "Cash",            # Метод оплаты
    "receipt_number": "R987654321"       # Номер чека
}

# 2. Создать словарь new_dict с 2 парами ключ: значение(отличные от первого словаря)
new_dict = {
    "price": 29.99,                      # Цена товара
    "quantity": 3,                       # Количество товара
    "item_id": "ABC123",                 # Идентификационный номер товара
    "date": "2023-08-20",                # Дата покупки
    "cashier": "John Smith",             # Имя кассира
    "discount": 10,                      # Скидка на товар в процентах
    "payment_method": "Credit Card",     # Метод оплаты
    "day_of_week": "Wednesday",          # День недели
    "receipt_number": "R123456789"       # Номер чека
}

# 3. Объединить два словаря через распаковку в новый словарь all_dict. Вывести его в терминал.
print("# 3. Объединить два словаря через распаковку в новый словарь all_dict. Вывести его в терминал.")

all_dict = {**my_dict, **new_dict}

print("all_dict =", all_dict)
print()

# 4. Изменить значение любого ключа в all_dict на '0' методом pop. Вывести в терминал изменённый словарь.
print("# 4. Изменить значение любого ключа в all_dict на '0' методом pop. Вывести в терминал изменённый словарь.")

print("all_dict =", all_dict.pop('price'))
print(all_dict)
print()

# 5. Удалить последнюю пару ключ: значение из словаря all_dict методом popitem.
print("# 5. Удалить последнюю пару ключ: значение из словаря all_dict методом popitem.")

all_dict.popitem()
print("all_dict =", all_dict)
print()

# 6. Создать список из 3 кортежей в которых по 2 значения.
print("# 6. Создать список из 3 кортежей в которых по 2 значения.")

list_of_tuples = [('item', 2), ("price", 4.95), ('name', 'Samsung')]
print()

# 7. Преобразовать этот список в словарь и вывести в терминал значение второго(позиция 1) ключа.
print("# 7. Преобразовать этот список в словарь и вывести в терминал значение второго(позиция 1) ключа.")

my_dict_1 = dict(list_of_tuples)

print("my_dict_1 =", my_dict_1)

print(list(my_dict_1.keys())[1][0])
