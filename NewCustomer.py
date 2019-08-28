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
        driver.find_element_by_xpath("/html/body/div[2]/a[2]").click()
        time.sleep(2)
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys("user2")
        elem = driver.find_element_by_name("first_name")
        elem.clear()
        elem.send_keys("Bruce")
        elem = driver.find_element_by_name("email")
        elem.clear()
        elem.send_keys("vasuparikh@gmail.com")
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("user1234")
        elem = driver.find_element_by_name("password2")
        elem.clear()
        elem.send_keys("user1234")
        driver.find_element_by_xpath("/html/body/form/p[6]/input").click()
        time.sleep(4)
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[2]/li[2]/a").click()
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys("user2")
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("user1234")
        driver.find_element_by_xpath("/html/body/form/button").click()
        elem = driver.find_element_by_name("entered_token")
        elem.clear()
        elem.send_keys(input("What is the token number:"))
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/div[2]/form/button").click()
        time.sleep(4)







    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
