import unittest
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BleacherReportSmokeTests(unittest.TestCase):

    @classmethod
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.maximize_window()
        inst.wait = WebDriverWait(inst.driver, 5)
        inst.driver.get('https://bleacherreport.com/')


    def test_homepage_title(self):
        self.assertEqual("Bleacher Report | Sports. Highlights. News. Now.", self.driver.title, "Verify that the title of the page is Bleacher Report")


    def test_navigation_bar(self):
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class = 'wide nav organism loaded']")))
            return True
        except TimeoutException:
            print("Navigation bar did not load")
            return False


    def test_loginpage(self):
        self.driver.find_element_by_class_name('login').click()
        try:
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[text()='Sign in with Phone']")))
            return True
        except TimeoutException:
            print("Login page did not load")
            return False


    @classmethod
    def tearDown(inst):
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()