import unittest

TEST_STAMP_1 = [
    {'offset': 0, 'score': {'away': 0, 'home': 0}},
    {'offset': 2, 'score': {'away': 0, 'home': 0}},
    {'offset': 4, 'score': {'away': 0, 'home': 0}},
    {'offset': 7, 'score': {'away': 1, 'home': 0}},
    {'offset': 9, 'score': {'away': 1, 'home': 0}},
    {'offset': 11, 'score': {'away': 1, 'home': 0}}
]
TEST_STAMP_2 = [
    {'offset': 3217, 'score': {'away': 0, 'home': 0}},
    {'offset': 3218, 'score': {'away': 0, 'home': 0}},
    {'offset': 3220, 'score': {'away': 0, 'home': 0}},
    {'offset': 3222, 'score': {'away': 1, 'home': 0}},
    {'offset': 3223, 'score': {'away': 1, 'home': 0}},
    {'offset': 3224, 'score': {'away': 1, 'home': 0}},
]
TEST_STAMP_3 = []


def get_score(game_stamps, offset):
    try:
        result = [dictionary for dictionary in game_stamps if dictionary["offset"] == offset]
        if not result: raise
    except:
        while True:
            offset -= 1
            result = [dictionary for dictionary in game_stamps if dictionary["offset"] == offset]
            if result: break
    values = [v for first_dict in result for k, v in first_dict.items()]
    away, home = values[1].values()
    return home, away


class TestGetScoreFunction(unittest.TestCase):

    def test_current_offset(self):
        # ожидаемый результат: 0 смещения счёт 0, 0
        expected_result = (0, 0)
        # фактический результат: по 0 смещению счёт 0, 0
        actual_result = get_score(TEST_STAMP_1, 6)
        self.assertEqual(expected_result, actual_result)

    def test_less_offset(self):
        # ожидаемый результат: по 8 смещения счёт 0, 1
        expected_result = (0, 1)
        # фактический результат: 8 смещения нет, по 7 смещению счёт 1, 0
        actual_result = get_score(TEST_STAMP_1, 8)
        self.assertEqual(expected_result, actual_result)

    def test_great_offset(self):
        # ожидаемый результат: по 15 смещения счёт 0, 1
        expected_result = (0, 1)
        # фактический результат: 15 смещения нет, по 11 смещению счёт 1, 0
        actual_result = get_score(TEST_STAMP_1, 15)
        self.assertEqual(expected_result, actual_result)

    def test_uncorrected_less_offset(self):
        # ожидаемый результат: по 3221 счёт 1, 0
        expected_result = (1, 0)
        # фактический результат: 3221 смещения нет, по 3220 смещению счёт 0, 0
        actual_result = get_score(TEST_STAMP_2, 3221)
        self.assertFalse(expected_result == actual_result)

    def test_uncorrected_grate_offset(self):
        # ожидаемый результат: по 3226 счёт 1, 1
        expected_result = (1, 1)
        # фактический результат: 3226 смещения нет, по 3224 смещению счёт 1, 0
        actual_result = get_score(TEST_STAMP_2, 3226)
        self.assertFalse(expected_result == actual_result)

    def test_get_score_with_negative_offset(self):
        # ожидаемый результат: по -5 смещению счёт 0, 0
        expected_result = (0, 0)
        # фактический результат: 3226 смещения нет, по 3224 смещению счёт 1, 0
        actual_result = get_score(TEST_STAMP_2, -5)
        with self.assertRaises(RuntimeError):
            get_score(expected_result, actual_result)
    
    def test_get_score_with_uncorrect_parameters(self):
        with self.assertRaises(TypeError):
            get_score()


if __name__ == '__main__':
    import sys
    import csv
    import operator
    reader = csv.reader(open("../python_dev/task3/allurls.csv"), delimiter=",")
    for product_url, price in reader:

        print(product_url)
        # sortedlist = sorted(reader, key=operator.itemgetter(1), reverse=True)
    unittest.main()
