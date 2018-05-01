import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Onspar_notifications_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log(self):
        user = "instructor"
        pwd = "password123"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://onspar.pythonanywhere.com/login")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        assert "Logged In"
        time.sleep(2)
        driver.get("http://onspar.pythonanywhere.com/notifications")
        time.sleep(5)
        driver.get("http://onspar.pythonanywhere.com/product/13/edit/")
        elem = driver.find_element_by_id("id_stock").clear()
        elem = driver.find_element_by_id("id_stock")
        elem.send_keys(3)
        driver.find_element_by_xpath("/html/body/div[2]/form/button").click()
        time.sleep(4)
        driver.get("http://onspar.pythonanywhere.com/notifications")
        time.sleep(10)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()