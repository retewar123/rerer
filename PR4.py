numbers = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers = set(numbers)

print("Множество:", unique_numbers)
print("Количество элементов:", len(unique_numbers))



my_set = {10, 20, 30}
my_set.add(40)      
my_set.remove(20) 

print("Результат:", my_set)



set_a = {1, 2, 3}
set_b = {3, 4, 5}

print("Объединение:", set_a | set_b)


set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Пересечение:", set_a & set_b)



set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Есть в первом, но нет во втором:", set_a - set_b)
print("Есть во втором, но нет в первом:", set_b - set_a)



set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print("Только в одном из множеств:", set_a ^ set_b)



my_set = {5, 10, 15, 20}
x = 15

print(x in my_set)



set_a = {1, 2}
set_b = {1, 2, 3, 4}

print("Является ли подмножеством:", set_a <= set_b)



text = "программирование"
unique_chars = set(text)

print("Уникальные символы:", unique_chars)
print("Количество различных символов:", len(unique_chars))



list_1 = [8, 3, 5, 3, 1, 9, 8]
list_2 = [5, 9, 2, 8, 5, 4]

common_sorted = sorted(set(list_1) & set(list_2))

print("Общие элементы по возрастанию:", common_sorted)
