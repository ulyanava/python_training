# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from python_training.group import Group

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class test_add_group2(unittest.TestCase):
    def setUp(self):
         self.wd = WebDriver(firefox_binary="C:/Program Files (x86)/Mozilla Firefox/firefox.exe")
         self.wd.implicitly_wait(90)

    #   for FirefoxESR
    #   self.wd = WebDriver(capabilities={"marionette": False},
    #   firefox_binary="C:/Program Files (x86)/Mozilla FirefoxESR/firefox.exe")

    def test_add_group2(self):
        wd = self.wd
        self.login(username="admin", password="secret")
        self.create_group_form(Group(name="name", header="header", footer="footer"))
        self.logout()

    def logout(self):
        wd = self.wd
        wd.find_element_by_link_text("Logout").click()

    def return_to_groups(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def create_group_form(self, group):
        wd = self.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill new group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups()

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def login(self, username, password):
        wd = self.wd
        self.open_home_page()
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()


    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
