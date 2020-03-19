import unittest
import yandex_translate


class TestYandexTranslate(unittest.TestCase):

    def test_translate_it_status_code(self):
        response = yandex_translate.translate_it('Проверка')
        self.assertEqual(response['code'], 200)

    def test_translate_correct(self):
        response = yandex_translate.translate_it('Привет')
        self.assertEqual(response['text'][0], 'Hi')

    def test_translate_language(self):
        response = yandex_translate.translate_it('Проверка языка')
        self.assertEqual(response['lang'], 'ru-en')

    def test_translate_q(self):
        """Проверка на ошибку вызова функции без аргумента"""
        with self.assertRaises(Exception):
            yandex_translate.translate_it()
