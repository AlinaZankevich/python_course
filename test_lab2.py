import unittest
import lab2_hw


class MyTestCase(unittest.TestCase):
    def test_select_sort(self):
        input_parameter = [-1, 0, 1, 2, 3, 4, -4]
        lab2_hw.select_sort(input_parameter)
        expected = [-4, -1, 0, 1, 2, 3, 4]
        self.assertEqual(expected, input_parameter)

    def test_select_sort_empty(self):
        input_parameter = []
        lab2_hw.select_sort(input_parameter)
        expected = []
        self.assertEqual(expected, input_parameter)

    def test_select_sort_equal_elements(self):
        input_parameter = [1, 1, 1, 1]
        lab2_hw.select_sort(input_parameter)
        expected = [1, 1, 1, 1]
        self.assertEqual(expected, input_parameter)


if __name__ == '__main__':
    unittest.main()
