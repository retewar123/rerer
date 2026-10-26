students = {"Алексей": 5, "Мария": 4, "Иван": 5}
print("Оценка Марии:", students["Мария"])


data = {"яблоко": 100, "банан": 80, "груша": 120}

data["апельсин"] = 150  
data["банан"] = 90      
del data["груша"]     

print(data)


info = {"имя": "Олег", "возраст": 20}
key = input("Введите ключ: ")

print(info.get(key, "Нет такого ключа"))


person = {"имя": "Анна", "город": "Москва", "профессия": "Дизайнер"}

print("Ключи:", list(person.keys()))
print("Значения:", list(person.values()))
print("Количество пар:", len(person))


products = {"Хлеб": 50, "Молоко": 90, "Сыр": 350}

for item, price in products.items():
    print(f"{item}: {price} руб.")


products = {"Хлеб": 50, "Молоко": 90, "Сыр": 350, "Кофе": 600}

total_price = sum(products.values())
most_expensive = max(products, key=products.get)

print("Сумма всех цен:", total_price)
print("Самый дорогой товар:", most_expensive)   


text = "программирование"
char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print(char_count)


text = "кот собака кот мышь собака кот слон"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_frequent = max(word_count, key=word_count.get)

print("Частота слов:", word_count)
print("Самое частое слово:", most_frequent)


original = {"a": 1, "b": 2, "c": 3}
swapped = {}

for key, value in original.items():
    swapped[value] = key

print(swapped)


countries = ["Россия", "Франция", "Япония", "Египет"]
capitals = ["Москва", "Париж", "Токио", "Каир"]

geo_dict = dict(zip(countries, capitals))

country = input("Введите название страны: ")
print(geo_dict.get(country, "Такой страны нет в списке"))