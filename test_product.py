import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Onspartest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()


# Test Script 1 - select product
   def test_add_product(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://onspar.pythonanywhere.com/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
       time.sleep(5)
       driver.get("http://onspar.pythonanywhere.com/shopping/")


       elem = driver.find_element_by_xpath("//*[@id='main']/div[1]/a[2]").click()
       driver.get("http://onspar.pythonanywhere.com/shopping/13/dell-inspiron-15-7200/Eng/")
       time.sleep(5)

       elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/form/div/div/button").click()
       time.sleep(3)
       # login to add to cart
       driver.get("http://onspar.pythonanywhere.com/cart/")
       time.sleep(3)
       user = "ajanet"
       pwd = "ajanet"
       driver = self.driver
       driver.maximize_window()
       driver.get("http://onspar.pythonanywhere.com/login/?next=/cart/add")
       elem = driver.find_element_by_id("id_username")
       elem.send_keys(user)
       elem = driver.find_element_by_id("id_password")
       elem.send_keys(pwd)
       time.sleep(4)
       elem.send_keys(Keys.RETURN)

       # test script 3 add to cart after authentication
       driver.get("http://onspar.pythonanywhere.com/home")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[2]/a").click()
       time.sleep(5)
       driver.get("http://onspar.pythonanywhere.com/shopping/")

       elem = driver.find_element_by_xpath("//*[@id='main']/div[1]/a[2]").click()
       driver.get("http://onspar.pythonanywhere.com/shopping/13/dell-inspiron-15-7200/Eng/")
       time.sleep(5)

       elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/form/div/div/button").click()

       elem = driver.find_element_by_xpath("/html/body/ul/li[2]/a").click()
# test case 4 checkout from cart
       time.sleep(5)
       #driver.get("http://onspar.pythonanywhere.com/cart/checkout/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("/html/body/div[2]/a").click()
       elem =driver.find_element_by_xpath("/html/body/form/input[12]").click()
       time.sleep(5)
      # elem = driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[2]/div/div/form/div/div/button").click()
       time.sleep(10)
       assert "Added to cart"


   def tearDown(self):
           self.driver.close()

if __name__ == "__main__":
       unittest.main()