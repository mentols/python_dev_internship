import math
import random

TIMESTAMPS_COUNT = 5000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


# функция генерации шага
def generate_stamp(previous_value):  # previous_value – прошлое состояние шага
    # изменение счёта игры
    # если вероятность больше чем 0.0001 – счёт увеличиваеться на 1
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    # добавляем 1 к счёту если есть такая возможность + вероятность больше чем 0.55
    home_score_change = 1 if score_changed and random.random() > 1 - PROBABILITY_HOME_SCORE else 0
    # добавляес 1 к счёту если есть такая возможность + счёт домашней команды не увлеичился
    away_score_change = 1 if score_changed and not home_score_change else 0

    # генерация шага
    # 1 - если в random() – от 0 до 0.33
    # 2 - если в random() – от 0.34 до 0.66
    # 3 - если в random() – от 0.67 до 0.99...
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    # возварашем следующий шаг с изменёнными состояниями
    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }


def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps


def get_score(game_stamps, offset):
    if offset < 0: raise
    '''
        Takes list of game's stamps and time offset for which returns the scores for the home and away teams.
        Please pay attention to that for some offsets the game_stamps list may not contain scores.
    '''
    try:
        # распаковываем списое со словарями и ищем нужное смещение
        result = [dictionary for dictionary in game_stamps if dictionary["offset"] == offset]
        # если смещение не найдено вбрасываем ошибку
        if not result: raise
    except:
        while True:
            # уменьшаем пока не найдём последнее доступное смещение
            offset -= 1
            result = [dictionary for dictionary in game_stamps if dictionary["offset"] == offset]
            if result: break
    # распаковываем словарь и берём словарь по ключю 'scope'
    values = [v for first_dict in result for k, v in first_dict.items()]
    # распаковываем словарь 'scopes'
    away, home = values[1].values()

    return home, away


game_stamps = generate_game()
TEST_STAMP_3 = []
print(get_score(TEST_STAMP_3, 0))
