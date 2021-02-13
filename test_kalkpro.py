import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Kalkpro(unittest.TestCase):
    # https://kalk.pro/finish/wallpaper/
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()
        # открытие страницы при начале каждого теста
        self.driver.get('https://kalk.pro/finish/wallpaper/')
        # ждем 10 сек до появления окна подтверждения согласия с COOKIE
        time.sleep(10)
        # находим крестик в появившемся окне
        elem = self.driver. \
            find_element_by_css_selector(".js--onclick-cookiePolicyAgree")
        # жмем на крестик
        elem.click()

    def tearDown(self):
        # закрытие браузера при окончании каждого теста
        self.driver.close()

    # вспомогательный метод для заполнения размеров комнаты
    def input_walls_data(self, hei, wid, len):
        driver = self.driver
        # высота
        # находим элемент страницы по ID
        elem = driver.find_element_by_id("js--roomСeiling_height")
        # очищаем элемент от старого значения
        elem.clear()
        # вносим новое значение
        elem.send_keys(hei)
        # ширина
        elem = driver.find_element_by_id("js--roomSizes_width")
        elem.clear()
        elem.send_keys(wid)
        # длина
        elem = driver.find_element_by_id("js--roomSizes_length")
        elem.clear()
        elem.send_keys(len)
    # метод для проверки работы калькулятора при различных
    # размерах комнаты, в т. ч. проверка отображения ошибок
    # при вводе некорректных данных
    def test_walls(self):
        driver = self.driver
        # пробуем ввести размер 1х1х1
        self.input_walls_data(1, 1, 1)
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # ждем 3 секунды, чтобы результаты расчета успели появиться
        time.sleep(3)
        # проверяем наличие результатов расчета
        self.assertIn('Результаты расчета', driver.page_source)
        # проверяем, что площадь четырех стех размером 1х1 равна 4
        elem = driver.find_element_by_css_selector(
            "ul.data-list li:nth-child(4) strong"
        )
        self.assertEqual('4 м²', elem.text)

        # пробуем ввести размер 0х1х1
        self.input_walls_data(0, 1, 1)
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # проверяем наличие сообщения об ошибке
        self.assertIn('Ошибки', driver.page_source)
        # проверяем наличие одной ссылки на поле ввода
        elems = driver.find_elements_by_css_selector(
            "a.js--onclick-goToField"
        )
        self.assertEqual(len(elems), 1)

        # пробуем ввести размер aхbхc (буквы вместо цифр)
        self.input_walls_data('a', 'b', 'c')
        # запускаем расчет
        elem = driver.find_element_by_class_name(
            "js--calcModelFormSubmit"
        )
        elem.click()
        # проверяем наличие сообщения об ошибке
        self.assertIn('Ошибки', driver.page_source)
        # проверяем наличие трех ссылок на поля ввода
        elems = driver.find_elements_by_css_selector(
            "a.js--onclick-goToField"
        )
        self.assertEqual(len(elems), 3)


if __name__ == '__main__':
    unittest.main()
