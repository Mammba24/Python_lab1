disk_size_mb = 1.44  # объем дискеты в Мб
pages = 100  # количество страниц в книге
lines_per_page = 50  # число строк на странице
chars_per_line = 25  # количество символов в строке
bytes_per_char = 4  # количество байт на один символ

# Перевод объема дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Расчет объема одной книги
book_size_bytes = pages * lines_per_page * chars_per_line * bytes_per_char

# Считаем, сколько книг поместится на дискете
books_on_disk = disk_size_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(books_on_disk))
