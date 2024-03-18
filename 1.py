# Импортируем библиотек
import csv

# Открываем входной файл game.txt на чтение
with open('game.txt', encoding='utf-8') as input_file:
    data = list(map(lambda x: x.strip().split('$'), input_file.readlines()))

# Список записей с ошибкой 55
records = []

# Проходимся по входным данным и составляем отсчет
for game_name, characters, name_error, date in data[1:]:
    if name_error.split(':')[-1] == '55':
        print(f'У персонажа\t{characters}\tв игре\t{game_name}\tнашлась ошибка с кодом:\t {name_error}.\tДата фиксации:\t {date}')
        records.append([characters, game_name, name_error, date])

# Меняем у полученных записей дату и значение ошибки
for record in records:
    record[2] = 'Done'
    record[3] = '0000-00-00'

# Открываем выходной файл game_new.csv на запись
with open('game_new.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter='$')
    writer.writerow(('characters', 'GameName' 'nameError', 'date'))
    writer.writerows(records)
