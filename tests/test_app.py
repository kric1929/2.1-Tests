import unittest
from unittest.mock import patch
import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.dirs, self.docs = app.update_date()
        with patch('app.update_date', return_value=(self.dirs, self.docs)):
            with patch('app.input', return_value='q'):
                app.secretary_program_start()

    def test_delete_doc(self):
        before_len = len(self.docs)
        with patch('app.input', return_value='10006'):
            app.delete_doc()
        self.assertLess(len(self.docs), before_len)

    def test_add_new_doc(self):
        before_len = len(self.docs)
        with patch('app.input', size_effect=['10007', 'passport', 'testUser', '1']):
            app.add_new_doc()
        self.assertGreater(len(self.docs), before_len)

    def test_get_doc_owner_name(self):
        name = 'Геннадий Покемонов'
        with patch('app.input', return_value='11-2'):
            return_name = app.get_doc_owner_name()
        self.assertEqual(return_name, name)

    def test_get_all_doc_owners_names(self):
        len_output = len(app.get_all_doc_owners_names())
        self.assertEqual(len_output, 3)

    def test_get_doc_shelf(self):
        number_shelf = '1'
        with patch('app.input', return_value='2207 876234'):
            return_shelf_number = app.get_doc_shelf()
        self.assertEqual(return_shelf_number, number_shelf)
