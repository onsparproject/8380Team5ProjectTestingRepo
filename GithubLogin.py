import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Onspar_notifications_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_log(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://onspar.pythonanywhere.com/login")
        driver.find_element_by_xpath("/html/body/div[2]/a[3]").click()
        elem = driver.find_element_by_name("login")
        elem.clear()
        elem.send_keys("vasuparikh")
        time.sleep(6)
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("vasu95guy")
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/form/div[2]/input[3]").click()
        time.sleep(7)




        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()