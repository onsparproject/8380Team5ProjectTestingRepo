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
        driver.get("http://onspar.pythonanywhere.com/product/create/")
        time.sleep(2)
        elem = driver.find_element_by_xpath("//select[@name='category']/option[text()='Phones']").click()
        elem = driver.find_element_by_id("id_name")
        elem.send_keys("Nextbit Robin")
        elem = driver.find_element_by_id("id_slug")
        elem.send_keys("nextbit-Robin")
        elem = driver.find_element_by_id("id_image")
        elem.send_keys("https://www.kickmobiles.com/content/images/thumbs/0006346_nextbit-robin-gsm-2afgx-robin-32gb-mint_420.jpeg")
        elem = driver.find_element_by_id("id_description")
        elem.send_keys("The Simple Yet Powerful Phone Yet. The Fast and Slim Android Phone")
        elem = driver.find_element_by_id("id_price")
        elem.send_keys("150")
        elem = driver.find_element_by_id("id_stock")
        elem.send_keys("15")
        driver.find_element_by_xpath("/html/body/div[2]/form/button").click()
        time.sleep(2)
        driver.get("http://onspar.pythonanywhere.com/notifications")
        time.sleep(6)

        def tearDown(self):
            self.driver.close()

    if __name__ == "__main__":
        unittest.main()