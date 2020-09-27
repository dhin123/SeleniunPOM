import unittest
from selenium import webdriver
import time
from Pageobjects.Loginpage import Loginpage

class LoginTest(unittest.TestCase):
    baseurl = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin"
    driver = webdriver.Chrome("C:\\Users\\sindh\\PycharmProject\\ChromeDriver\\chromedriver.exe")

    @classmethod
    def setUpClass(cls):
        cls.driver.get(cls.baseurl)
        cls.driver.maximize_window()

    def test_login(self):
        lp = Loginpage(self.driver)
        lp.username(self.username)
        lp.password(self.password)
        lp.login()
        time.sleep(3)
        self.assertEqual("Dashboard /nopCommerce administartion", self.driver.title, "Result")