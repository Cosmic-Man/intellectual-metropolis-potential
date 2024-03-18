# Импортируем библиотек
import csv
import string


def hash_map():
    """
    Создает хэш-таблицу перевода символа в число по правилу
    :return: хэш-таблица перевода
    """
    letters = string.ascii_letters + string.digits + ':' + '-'
    hash_letters = {}
    letter_translate, digits_translate, two_dots, minus = 1, 53, 64, 65

    for symbol in letters:
        if symbol.isalpha():
            hash_letters[symbol] = letter_translate
            letter_translate += 1
        elif symbol == '0':
            hash_letters[symbol] = 63
        elif symbol.isdigit():
            hash_letters[symbol] = digits_translate
            digits_translate += 1
        elif symbol == ':':
            hash_letters[symbol] = two_dots
        elif symbol == '-':
            hash_letters[symbol] = minus
    return hash_letters


# хэш-таблица перевода символа в число
letters_hash_map = hash_map()


def prepare_for_hashing(game_name):
    """
    Преобразует строку для последующей генерации хэша
    :param game_name: входная строка в формате: название игры + имя персонажа
    :return: строчка по правилу
    """
    return game_name.replace(' ', '')


def get_hash(s):
    """
    Создает хэш для строки по правилу
    :param s: строка в формате: название игры + имя персонажа
    :return: хэш значение
    """
    p = 65
    m = 10 ** 9 + 9
    s = prepare_for_hashing(s[0] + s[1])
    return sum([(letters_hash_map.get(s[i], 0) * p ** i) % m for i in range(len(s))])


# Открываем входной файл game.txt на чтение
with open('game.txt', encoding='utf-8') as input_file:
    data = list(map(lambda x: x.strip().split('$'), input_file.readlines()))


# Проходимся по входным данным и добавляем к каждой строке хэш значение
for i in range(1, len(data)):
    data[i] = [get_hash(data[i])] + data[i]


# Открываем выходной файл game_with_hash.csv на запись
with open('game_with_hash.csv', 'w', newline='', encoding='utf-8') as output_file:
    writer = csv.writer(output_file, delimiter='$')
    writer.writerow(('hash', 'GameName', 'characters' 'nameError', 'date'))
    writer.writerows(data[1:])
