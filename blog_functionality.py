import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Onspartest(unittest.TestCase):

   def setUp(self):
       self.driver = webdriver.Chrome()

# Test Script 1 - login to create new post in blog
   def test_check_blog(self):
       driver = self.driver
       driver.maximize_window()
       driver.get("http://onspar.pythonanywhere.com/")
       time.sleep(5)
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[3]/a").click()
       time.sleep(5)
       driver.get("http://onspar.pythonanywhere.com/blog/")


       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[2]/li[2]/a").click()
       driver.get("http://onspar.pythonanywhere.com/login/")
       time.sleep(5)
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

       driver.get("http://onspar.pythonanywhere.com/home")
       elem = driver.find_element_by_xpath("//*[@id='myNavbar']/ul[1]/li[3]/a").click()
       time.sleep(5)
       driver.get("http://onspar.pythonanywhere.com/blog/")
       elem = driver.find_element_by_xpath("/html/body/div[2]/a").click()
       title = "unittest1"
       text ="unittest1"
       time.sleep(4)
       elem = driver.find_element_by_id("id_title")
       elem.send_keys(title)
       elem = driver.find_element_by_id("id_text")
       elem.send_keys(text)
       time.sleep(4)
       elem.find_element_by_xpath("/html/body/form/button").click()
       time.sleep(4)

       assert "blog created "

