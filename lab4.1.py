import json

def task() -> float:
    # Считываем данные из файла input.json
    with open('input.json', 'r') as file:
        data = json.load(file)

    # Вычисляем сумму произведений
    total_sum = sum(d['score'] * d['weight'] for d in data)

    # Возвращаем результат, округленный до 3 знаков
    return round(total_sum, 3)

# Вызов функции и вывод результата
print(task())


