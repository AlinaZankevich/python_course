import unittest


# class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertEqual(True, True)


def full_name(last, first, middle):
    #     soedinaem fio
    full = last+" "+first+" "+middle
    #vozvrashaem FIO s bolshou bukvi
    return full.title()






if __name__ == '__main__':
    unittest.main()
