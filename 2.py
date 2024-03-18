# Открываем входной файл game.txt на чтение
with open('game.txt', encoding='utf-8') as input_file:
    data = list(map(lambda x: x.strip().split('$'), input_file.readlines()))


def quick_sort(massive):
    """
    Сортирует матрицу по столбцу игры
    :param massive: матрица
    :return: отсортированная матрица
    """
    
    if len(massive) < 2:
        return massive
    else:
        pivot = massive[0]
        less = [i for i in massive if i[0] < pivot[0]]
        equal = [i for i in massive if i[0] == pivot[0]]
        greater = [i for i in massive if i[0] > pivot[0]]
        return quick_sort(less) + equal + quick_sort(greater)


# Получаем отсортированный список по столбцу игры
sorted_data = quick_sort(data[1:])

# Словарь игр с количеством их багов
games_bugs = {}

# номер игры
n = 1

# Проходимся по отсортированным данным для заполнения game_bugs
for game_name, characters, name_error, date in sorted_data:
    games_bugs[game_name] = games_bugs.get(game_name, 0) + 1

# Выводим отсчет по багам в играх
for game_name, count_bugs in games_bugs.items():
    print(f'<Игра {n}> - количество багов: {count_bugs}')
    n += 1
