import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, n):
    return a ** n

def square_root(a):
    return math.sqrt(a)

def cos(a):
    return math.cos(a)

def sin(a):
    return math.cos(a)

def tan(a):
    return math.tan(a)

def factorial(a):
    result = 1
    for i in range(1, a + 1):
        result *= i
    return result

while True:
    print("Выберите операцию:")
    print("1. Сложить 2 числа")
    print("2. Вычесть первое из второго")
    print("3. Перемножить два числа")
    print("4. Разделить первое на второе")
    print("5. Возвести в степень N первое число")
    print("6. Найти квадратный корень из числа")
    print("7. найти косинус")
    print("8. Найти синус")
    print("9. Найти тангенс")
    print("10. Найти факториал")
    print("11. Выйти из программы")

    choice = input("Введите номер операции: ")

    if choice == "11":
        break

    while True:
        try:
            num1 = float(input("Введите первое число: "))
            num2 = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Ошибка: введите числа")

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        if num2 != 0:
            result = divide(num1, num2)
        else:
            print("Ошибка: деление на ноль")
            continue
    elif choice == "5":
        result = power(num1, num2)
    elif choice == "6":
        if num1 >= 0:
            result = square_root(num1)
        else:
            print("Ошибка: извлечение квадратного корня из отрицательного числа")
            continue
    elif choice == "7":
        result = cos(num1)
    elif choice == "8":
        result = sin(num1)
    elif choice == "9":
        result = tan(num1)

    elif choice == "10":
        if num1 >= 0 and num1.is_integer():
            result = factorial(int(num1))
        else:
            print("Ошибка: вычисление факториала неположительного числа или числа с десятичной частью")
            continue
    else:
        print("Ошибка: некорректный номер операции")
        continue

    print("Результат:", result)
    print("")

print("Программа завершена")
