# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re



class AppDynamicsJob(unittest.TestCase):
    def setUp(self):

        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_app_dynamics_job(self):
        wd = self.wd
        wd.get("http://demowebshop.tricentis.com/")
        self.Login(wd)
        wd.find_element_by_link_text("Computers").click()
        wd.find_element_by_xpath("//img[@alt='Picture for category Notebooks']").click()
        wd.find_element_by_xpath("//input[@value='Add to cart']").click()
        # wd.find_element_by_xpath("//li[@id='topcartlink']/a/span").click()

        wd.find_element_by_link_text("Books").click()
        wd.find_element_by_link_text("Fiction").click()
        wd.find_element_by_xpath("//input[@value='Add to cart']").click()

        self.LogOut(wd)

    def LogOut(self, wd):
        wd.find_element_by_link_text("Log out").click()

    def Login(self, wd):
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("Email").send_keys("qakostina@gmail.com")
        wd.find_element_by_id("Password").send_keys("test2test")
        wd.find_element_by_xpath("//input[@value='Log in']").click()


if __name__ == "__main__":
    unittest.main()
