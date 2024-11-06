def find_common_participants(group1, group2, separator=','):
    # Разбиваем строки на списки участников по заданному разделителю
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))

    # Находим пересечение и сортируем результат
    common_participants = sorted(participants1 & participants2)

    return common_participants


# Проверяем работу функции с разделителем отличным от запятой
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common)
