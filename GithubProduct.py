import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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
        driver.find_element_by_xpath("/html/body/nav/div/div/ul[1]/li[2]/a").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[3]/div[1]/a[2]").click()
        time.sleep(20)
        elem = Select(driver.find_element_by_id("id_quantity"))
        elem.select_by_value("2")
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/form/div/div/button").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/ul/li[2]/a").click()
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[2]/a").click()
        time.sleep(10)
        driver.find_element_by_xpath("/html/body/form/input[12]").click()
        time.sleep(15)
        elem = driver.find_element_by_name("login_email")
        elem.clear()
        elem.send_keys("vparikh-buyer@unomaha.edu")
        time.sleep(15)
        elem = driver.find_element_by_id("btnNext")
        elem.click()
        time.sleep(10)
        elem = driver.find_element_by_name("login_password")
        elem.clear()
        elem.send_keys("test1234")
        time.sleep(15)
        elem = driver.find_element_by_id("btnLogin")
        elem.click()
        time.sleep(7)
        elem = driver.find_element_by_id("confirmButtonTop")
        elem.click()
        time.sleep(17)
        elem = driver.find_element_by_id("merchantReturnBtn")
        elem.click()
        time.sleep(7)




        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()