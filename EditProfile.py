import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class Test_OMK(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # Employee Login to the OMK website.
    def test_omk_employee(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://onspar.pythonanywhere.com/login/")
        driver.find_element_by_xpath("/html/body/div[2]/a[3]").click()
        time.sleep(2)
        elem = driver.find_element_by_name("login")
        elem.clear()
        elem.send_keys("vasuparikh")
        time.sleep(2)
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("vasu95guy")
        elem = driver.find_element_by_name("commit")
        elem.click()
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[2]/li[2]/a").click()
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/div[2]/a").click()
        time.sleep(7)
        elem = driver.find_element_by_name("address")
        elem.clear()
        elem.send_keys("3031 S 70th Street")
        elem = driver.find_element_by_name("zipcode")
        elem.clear()
        elem.send_keys("68106")
        driver.find_element_by_xpath("/html/body/div[2]/form/button").click()
        time.sleep(8)
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[2]/li[2]/a").click()
        time.sleep(8)






    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()