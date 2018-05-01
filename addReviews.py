import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Onspar_addReviews_Test(unittest.TestCase):

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
        driver.get("http://onspar.pythonanywhere.com/shopping/13/dell-inspiron-15-7200/Eng/")
        time.sleep(2)
        driver.get("http://onspar.pythonanywhere.com/shopping/addReview/13/")
        elem = driver.find_element_by_id("id_title")
        elem.send_keys("Not Good")
        elem = driver.find_element_by_id("id_text")
        elem.send_keys("Not so good laptop. It is very bulky and is really slow")
        driver.find_element_by_xpath("/html/body/div[2]/form/button").click()
        time.sleep(2)
        driver.get("http://onspar.pythonanywhere.com/shopping/13/dell-inspiron-15-7200/Eng/")
        time.sleep(20)
        driver.get("http://onspar.pythonanywhere.com/shopping/13/French/")
        time.sleep(10)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()