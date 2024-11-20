import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    # Считываем содержимое CSV файла
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        reader = csv.DictReader(csv_file)  # Преобразует строки CSV в словари
        data = [row for row in reader]  # Собираем все строки в список

    # Записываем данные в JSON файл с отступами 4
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Выполняем конвертацию
    task()

    # Проверяем содержимое выходного файла
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

