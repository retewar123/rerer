print("Доступные операции:")
print("1. Арифметика: +, -, *, /, //, %, **")
print("2. Сравнение: ==, !=, >, <, >=, <=")
print("3. Логические: and, or, not")

operator = input("\nВведите нужный оператор из списка выше: ")

if operator == 'not':
  num = float(input("Введите число (0 расценивается как False, любое другое — как True): "))
  result = not bool(num)
  print(f"Результат: not {num} = {result}")

else:
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result = "Ошибка: Деление на ноль!"
        else:
            result = num1 / num2
    elif operator == '//':
        if num2 == 0:
            result = "Ошибка: Деление на ноль!"
        else:
            result = num1 // num2
    elif operator == '%':
        if num2 == 0:
            result = "Ошибка: Деление на ноль!"
        else:
            result = num1 % num2
    elif operator == '**':
        result = num1 ** num2

    elif operator == '==':
        result = num1 == num2
    elif operator == '!=':
        result = num1 != num2
    elif operator == '>':
        result = num1 > num2
    elif operator == '<':
        result = num1 < num2
    elif operator == '>=':
        result = num1 >= num2
    elif operator == '<=':
        result = num1 <= num2

    elif operator == 'and':
        result = bool(num1) and bool(num2)
    elif operator == 'or':
        result = bool(num1) or bool(num2)
        
    else:
        result = "Ошибка: Введен неизвестный оператор!"

print(f"Результат: {result}")