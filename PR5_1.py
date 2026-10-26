for i in range(1, 11):
    print(i, end=" ")


for i in range(2, 51, 2):
    print(i, end=" ")


for i in range(10, 0, -1):
    print(i, end=" ")


n = int(input("Введите число n: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Сумма:", total)


n = int(input("Введите число n: "))
factorial = 1

for i in range(1, n + 1):
    factorial *= i

print(f"Факториал {n}! =", factorial)


n = int(input("Введите число n: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


numbers = [-5, 3, 0, 12, -1, 8, 4]
count = 0

for num in numbers:
    if num > 0:
        count += 1

print("Количество положительных чисел:", count)


text = "Привет, как дела? Hello World!"
vowels = "аеёиоуыэюяaeiouy"
count = 0

for char in text.lower():
    if char in vowels:
        count += 1

print("Количество гласных:", count)


numbers = [14, -3, 42, 8, 99, 23, 5]
max_num = numbers[0]

for num in numbers:
    if num > max_num:
        max_num = num

print("Наибольший элемент:", max_num)


for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:2}", end=" ")
    print()