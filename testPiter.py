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
        wd.get("https://www.piter.com/")
        wd.find_element_by_link_text(u"Войти").click()
        wd.find_element_by_id("email").send_keys("qakostina@gmail.com")
        wd.find_element_by_id("password").send_keys("test2er")

        # wd.find_element_by_link_text(u"ВОЙТИ").click()
        #wd.find_element_by_name("commit").click() #лучше
        # wd.find_element_by_xpath(
        #      u"(.//*[normalize-space(text()) and normalize-space(.)='Вход в кабинет покупателя'])[2]/following::div[5]").click()
        wd.find_element_by_xpath("//input[@name='commit']").click()
        wd.find_element_by_xpath(
            "(.//*[normalize-space(text()) and normalize-space(.)='(800) 500 42 17'])[1]/following::span[1]").click()
        wd.find_element_by_link_text(u"Кабинет покупателя").click()
        wd.find_element_by_link_text(u"Выход").click()

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    # def close_alert_and_get_its_text(self):
    #     try:
    #         alert = self.driver.switch_to_alert()
    #         alert_text = alert.text
    #         if self.accept_next_alert:
    #             alert.accept()
    #         else:
    #             alert.dismiss()
    #         return alert_text
    #     finally:
    #         self.accept_next_alert = True

    # def tearDown(self):
    #     # To know more about the difference between verify and assert,
    #     # visit https://www.seleniumhq.org/docs/06_test_design_considerations.jsp#validating-results
    #     self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()