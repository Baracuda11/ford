def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()                               # Вызов функции без аргументов
print_params(5, 'pyramid', False)   # Вызов функции с тремя аргументами
print_params(466, 'водопад')           # Вызов функции с двумя аргументами + 1 по умолчанию
print_params(b = 'экзамен')                  # Вызов функции с одним аргументом + 2 по умолчанию
print_params(b = 25)
print_params(c = [1, 2, 3])

# 2. Распакоука на%;№ (」°ロ°)」
values_list = [458, 'вода', False]
values_dict = {'a': 500, 'b': 'стол', 'c': True}
print_params(*values_list)
print_params(**values_dict)


# 3. Распаковка - параметры:
values_list_2 = [54.32, 'строка']
print_params(*values_list_2, 42)

