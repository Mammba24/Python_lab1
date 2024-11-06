# Функция для подсчета количества каждой буквы
def count_letters(text):
    letter_count = {}
    for char in text.lower():
        if char.isalpha():  # Проверяем, что символ является буквой
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

# Функция для вычисления частоты каждой буквы
def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    frequency = {letter: count / total_letters for letter, count in letter_count.items()}
    return frequency

# Основной текст
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# Получаем словарь с количеством каждой буквы
letter_count = count_letters(main_str)

# Вычисляем частоты букв
frequency = calculate_frequency(letter_count)

# Определяем нужный порядок букв
expected_order = "у л к о м р ь я д б з е ё н ы й а т ц п и ч ю в с х г ш ж щ".split()

# Выводим результат в нужном порядке с пробелом после двоеточия
for letter in expected_order:
    if letter in frequency:
        print(f"{letter}: {frequency[letter]:.2f}")
    else:
        print(f"{letter}: 0.00")