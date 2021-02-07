import unittest
import lab1


class MyTestCase(unittest.TestCase):
    def test_ticket_is_lucky(self):
        expected = True
        result = lab1.ticket_is_lucky(700000)
        self.assertEqual(expected, result)

    def test_ticket_is_not_lucky(self):
        expected = False
        result = lab1.ticket_is_lucky(700001)
        self.assertEqual(expected, result)

    def test_ticket_together(self):
        expected = True
        result = lab1.task2()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
