import unittest
import lab2_hw


class MyTestCase(unittest.TestCase):
    def test_select_sort(self):
        input_parametr = [-1, 0, 1, 2, 3, 4, -4]
        lab2_hw.select_sort(input_parametr) 
        expected = [-4, -1, 0, 1, 2, 3, 4]
        self.assertEqual(expected, input_parametr)


if __name__ == '__main__':
    unittest.main()
