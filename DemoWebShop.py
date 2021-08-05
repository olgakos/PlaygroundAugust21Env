# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re



class AddToCardTests(unittest.TestCase):
    def setUp(self):

        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)


    def test_add_to_card(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="qakostina@gmail.com", password="test2test")
        self.add_to_card(wd)
        self.log_out(wd)

    def open_home_page(self, wd):
        wd.get("http://demowebshop.tricentis.com/")

    def add_to_card(self, wd): #добавляем в корзину 2 товара
        wd.find_element_by_link_text("Computers").click() #Перешли в раздел товаров 1
        wd.find_element_by_xpath("//img[@alt='Picture for category Notebooks']").click() #выбрали товар по картинке
        wd.find_element_by_xpath("//input[@value='Add to cart']").click() #кнопка Добавить в корзину
        # wd.find_element_by_xpath("//li[@id='topcartlink']/a/span").click()
        wd.find_element_by_link_text("Books").click() #Перешли в раздел товаров 2
        wd.find_element_by_link_text("Fiction").click() #выбрали товар по названию-ссылке
        wd.find_element_by_xpath("//input[@value='Add to cart']").click() #кнопка Добавить в корзину

    def log_out(self, wd):
        wd.find_element_by_link_text("Log out").click()

    def login(self, wd, username, password):
        wd.find_element_by_link_text("Log in").click()
        wd.find_element_by_id("Email").send_keys(username)
        wd.find_element_by_id("Password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Log in']").click()


if __name__ == "__main__":
    unittest.main()
