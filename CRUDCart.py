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
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys("user2")
        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys("user1234")
        driver.find_element_by_xpath("/html/body/form/button").click()
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[1]/li[2]/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/a[2]").click()
        time.sleep(3)
        elem = Select(driver.find_element_by_id("id_quantity"))
        elem.select_by_value("2")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/form/div/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/ul/li[1]/a").click()
        driver.find_element_by_xpath("/html/body/div[3]/div[2]/a[2]").click()
        time.sleep(3)
        elem = Select(driver.find_element_by_id("id_quantity"))
        elem.select_by_value("1")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/form/div/div/button").click()
        time.sleep(7)
        elem = Select(driver.find_element_by_name("quantity"))
        elem.select_by_value("2")
        driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[3]/form/input[2]").click()
        time.sleep(6)
        driver.find_element_by_xpath("/html/body/table/tbody/tr[2]/td[4]/a").click()
        time.sleep(5)


