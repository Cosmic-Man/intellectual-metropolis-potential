# Импортируем библиотек
import csv

# Открываем входной файл game.txt на чтение
with open('game.txt', encoding='utf-8') as input_file:
    data = list(map(lambda x: x.strip().split('$'), input_file.readlines()))

# Словарь игр с количеством их ошибок
games_errors = {}


# Проходимся по отсортированным данным для заполнения games_errors
for game_name, characters, name_error, date in data[1:]:
    games_errors[game_name] = games_errors.get(game_name, 0) + 1

# Матрица с новым столбцом counter
new_data = []

# Проходимся по входным данным для заполнения матрицы new_data
for game_name, characters, name_error, date in data[1:]:
    new_data.append([game_name, characters, name_error, date, games_errors[game_name]])
new_data.insert(0, data[0] + ['counter'])


# Открываем выходной файл game_counter.csv на запись
with open('game_counter.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter='$')
    writer.writerows(new_data)
