def month_to_season(num):
    if (num in range(1, 3)) or num == 12:
        return ("Зима")
    elif num in range(3, 6):
        return ("Весна")
    elif num in range(6, 9):
        return ("Лето")
    elif num in range(9, 12):
        return ("Осень")
    else:
        return ("Ошибка, введено неправильно значение")
