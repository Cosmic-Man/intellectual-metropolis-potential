# Открываем входной файл game.txt на чтение и сортируем в алфавитном порядке по столбцу персонажи
with open('game.txt', encoding='utf-8') as input_file:
    data = list(map(lambda x: x.strip().split('$'), input_file.readlines()))
    data.sort(key=lambda x: x[1])


def binary_search(array, element):
    """
    # Находит игры в которых появлялся персонаж
    :param array: отсортированный список значений для поиска
    :param element: искомое значение
    :return: игры
    """

    low, high = 0, len(array) - 1
    while low <= high:
        middle = (low + high) // 2
        guess = array[middle][1]
        if guess == element:
            yield array[middle][0]
        if guess > element:
            high = middle - 1
        else:
            low = middle + 1


# Вводим имя персонажа
input_character = input()

# Ищем 5 игр, где он появлялся
while input_character != 'game':
    found_games = list(binary_search(data, input_character))
    if found_games:
        print(f'Персонаж {input_character} встречается в играх')
        for game in found_games[:5]:
            print(game)
        if len(found_games) > 5:
            print('и др.')
    else:
        print(f'Этого персонажа не существует')
    input_character = input()


