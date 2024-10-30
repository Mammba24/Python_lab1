# Исходные данные
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# Инициализация переменных
required_capital = 0
current_spend = spend

# Расчет
for _ in range(months):
    # Определяем необходимую сумму для покрытия разницы между расходами и зарплатой
    required_capital += max(0, current_spend - salary)

    # Увеличиваем расходы на 3% для следующего месяца
    current_spend *= (1 + increase)

# Округляем итоговую подушку безопасности до целого числа
required_capital = round(required_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", required_capital)
