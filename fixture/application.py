from selenium.webdriver.firefox.webdriver import WebDriver

from python_training.fixture.contact import ContactHelper
from python_training.fixture.group import GroupHelper
from python_training.fixture.session import SessionHelper


class Application:
    # конструктор
    def __init__(self):
        # инициализация (запуск браузера)
        self.wd = WebDriver(firefox_binary="C:/Program Files (x86)/Mozilla Firefox/firefox.exe")
        self.wd.implicitly_wait(90)
        # инициализация помощников
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    #   for FirefoxESR
    #   self.wd = WebDriver(capabilities={"marionette": False},
    #   firefox_binary="C:/Program Files (x86)/Mozilla FirefoxESR/firefox.exe")

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()
