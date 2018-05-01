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
        driver.find_element_by_xpath("/html/body/div[2]/a[1]").click()
        time.sleep(6)
        elem = driver.find_element_by_name("identifier")
        elem.clear()
        elem.send_keys("onsparwebsite")
        elem.send_keys(Keys.RETURN)
        time.sleep(6)
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("onspar@1234")
        elem.send_keys(Keys.RETURN)
        time.sleep(10)



        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()