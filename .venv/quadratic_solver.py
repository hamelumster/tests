import math


def solve_quadratic_equation(a, b, c):
    # Вычисление дискриминанта
    discriminant = b ** 2 - 4 * a * c

    # Проверка дискриминанта и вычисление корней
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return root, None
    else:
        return None, None


# Функция для печати результатов
def solve_and_print_quadratic_equation():
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))

    roots = solve_quadratic_equation(a, b, c)

    if roots[0] is not None and roots[1] is not None:
        print(f"Корни уравнения: {roots[0]} и {roots[1]}")
    elif roots[0] is not None:
        print(f"Уравнение имеет один корень: {roots[0]}")
    else:
        print("Уравнение не имеет действительных корней")


# Вызов функции
solve_and_print_quadratic_equation()