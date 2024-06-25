def findFirstBrokenVersion(n: int) -> int:
    left, right = 1, n
    while left < right:
        mid = (left + right) // 2
        if isBrokenVersion(mid):
            right = mid  # продолжаем искать в левой половине
        else:
            left = mid + 1  # продолжаем искать в правой половине
    return left  # или right, т.к. они равны

# Пример использования
# Предположим, что функция isBrokenVersion уже определена
def isBrokenVersion(version: int) -> bool:
    # примерная реализация для демонстрации
    first_broken = 4  # например, первая сломанная версия - 4
    return version >= first_broken

# Вызов функции
n = 10
print(findFirstBrokenVersion(n))  # Вывод: 4
