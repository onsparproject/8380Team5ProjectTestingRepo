import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class Test_OMK(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Employee Login to the OMK website.
    def test_omk_employee(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://onspar.pythonanywhere.com/login/")
        driver.find_element_by_xpath("/html/body/div[2]/a[1]").click()
        time.sleep(2)
        elem = driver.find_element_by_name("identifier")
        elem.clear()
        elem.send_keys("onsparwebsite")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("onspar@1234")
        time.sleep(2)
        elem.send_keys(Keys.RETURN)
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[1]/li[2]/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/a[2]").click()
        time.sleep(3)
        elem = Select(driver.find_element_by_id("id_quantity"))
        elem.select_by_value("2")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/form/div/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/ul/li[2]/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/form/input[12]").click()
        time.sleep(10)


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()