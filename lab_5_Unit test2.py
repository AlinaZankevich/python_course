import unittest
import lab_5_full_name


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        result = lab_5_full_name.full_name('Zankevich', 'Alina', 'Alexandrovna')# result - eto vsegda
        #ssilka na modul i funkciu v nem v skobkah vhodnie parametri
        expected = 'Zankevich Alina Alexandrovna'
        self.assertEqual(result, expected)

    def test_big(self):
        result = lab_5_full_name.full_name('ZANKEVICH', 'ALINA', 'ALEXANDROVNA')
        expected = 'Zankevich Alina Alexandrovna'
        self.assertEqual(result, expected)

    def test_small(self):
        result = lab_5_full_name.full_name('zankevich', 'alina', 'alexandrovna')
        expected = 'Zankevich Alina Alexandrovna'
        self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
