import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        # запуск Firefox при начале каждого теста
        self.driver = webdriver.Firefox()

    def tearDown(self):
        #     закрытие браузера при окончании каждого теста
        self.driver.close()

    def test_search_in_superlogoped_com(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.superlogoped.com
        driver.get("http://www.superlogoped.com")
        # проверка наличия слова Логопед в заголовке страницы
        self.assertIn("Логопед", driver.title)
        # ждем 5 секунд

        enter_button = driver.find_element_by_link_text("Войти")
        enter_button.click()

        time.sleep(2)

        username = driver.find_element_by_xpath('//input[@name="username"]')
        username.send_keys("mylogin")

        password = driver.find_element_by_xpath("//input[@name='password']")
        password.send_keys("qwerty123")

        time.sleep(2)

        enter_button2 = driver.find_element_by_xpath("//input[@name='Login']")
        enter_button2.click()

        time.sleep(2)

        profile_element = driver.find_element_by_xpath("//h1[text()='Alina Zankevich']")

        time.sleep(5)

    def test_login_logout(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org/psf-landing/
        # на которой есть кнопка Sign In
        driver.get("https://www.python.org/psf-landing/")
        # ждем 5 секунд
        time.sleep(5)
        # поиск ссылки с текстом "Sign In"
        elem = driver.find_element_by_link_text("Sign In")
        # нажатие на ссылку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода логина по XPath
        # (тег input с name='login')
        elem = driver.find_element_by_xpath("//input[@name='login']")
        # ввод логина
        elem.send_keys("AlinaZankevich")
        # ждем 5 секунд
        time.sleep(5)
        # поиск текстового поля для ввода пароля по XPath
        # (тег input с name='password')
        elem = driver.find_element_by_xpath("//input[@name='password']")
        # ввод логина
        elem.send_keys("python123")
        # ждем 5 секунд
        time.sleep(5)
        # жмем ввод для отправки формы
        elem.send_keys(Keys.RETURN)
        # ждем 5 секунд
        time.sleep(5)
        # проверка наличия на странице строки "Your account"
        # после входа
        self.assertIn("Your account", driver.page_source)
        # ждем 5 секунд
        time.sleep(5)

        driver.get("https://www.python.org/accounts/logout/")

        # поиск кнопки на форме в главной области страницы
        # по CSS-селектору
        elem = driver.find_element_by_css_selector(
            'div.container section.main-content form button'
        )  # нажатие на кнопку
        elem.click()
        # ждем 5 секунд
        time.sleep(5)
        # проверка отсутствия на странице строки "Your account"
        # после выхода
        self.assertNotIn("Your account", driver.page_source)

    def test_about_breadcrumbs(self):
        driver = self.driver
        # открытие в Firefox страницы http://www.python.org
        driver.get("http://www.python.org")
        # получаем список ссылок в меню About по CSS-селектору
        elems = driver.find_elements_by_css_selector('#about ul li a')
        # перебираем полученные подпункты меню,
        # выписываем названия и ссылки в отдельные списки
        # потому что при переходе по ссылкам на другие страницы
        # связь со списком подпунктов будет потеряна
        href_list = []
        name_list = []
        for e in elems:
            href_list.append(e.get_attribute("href"))
            name_list.append(e.get_attribute('innerHTML'))

        # перебираем полученные ссылки
        for i in range(len(href_list) - 1):
            # переходим по ссылке
            driver.get(
                href_list[i]
            )
            # получаем строчку хлебных крошек
            elem = driver.find_element_by_css_selector('.breadcrumbs')
            # проверка наличия в хлебных крошках ссылки на пункт About
            self.assertIn("About", elem.get_attribute('innerHTML'))
            # проверка наличия в хлебных крошках
            # наличия названия текущего пункта
            self.assertIn(
                # название текущего пункта
                name_list[i],
                # строчка хлебных крошек
                elem.get_attribute('innerHTML')
            )
            # ждем 5 секунд
            time.sleep(3)


class PythonOrgSearchChromium(PythonOrgSearch):
    def setUp(self):
        self.driver = webdriver.Chrome()


if __name__ == '__main__':
    unittest.main()
