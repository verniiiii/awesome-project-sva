# Калькулятор геометрических вычислений
import math

def calculate_hypotenuse(a, b):
    """
    Вычисляет длину гипотенузы прямоугольного треугольника
    по двум катетам
    """
    return math.sqrt(a**2 + b**2)

def calculate_area(a, b):
    """
    Вычисляет площадь прямоугольного треугольника
    по двум катетам
    """
    return 0.5 * a * b

def main():
    """Основная функция программы"""
    print("Калькулятор геометрических вычислений")
    print("=====================================")
    
    try:
        # Ввод данных
        a = float(input("Введите длину первого катета: "))
        b = float(input("Введите длину второго катета: "))
        
        # Вычисления
        hypotenuse = calculate_hypotenuse(a, b)
        area = calculate_area(a, b)
        
        # Вывод результатов
        print(f"\nРезультаты вычислений:")
        print(f"Длина гипотенузы: {hypotenuse:.2f}")
        print(f"Площадь треугольника: {area:.2f}")
        
    except ValueError:
        print("Ошибка! Введите числовые значения.")

if __name__ == "__main__":
    main()