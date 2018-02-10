# -*- coding: utf-8 -*-

import pytest

from python_training.fixture.application import Application
from python_training.model.contact import Contact


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_test_contact_group(app):
    app.session.login(username="admin", password="secret")
    app.add_contact(Contact(first_name="Tania", middle_name="TU", last_name="Ulyanava",
                            nickname="tatianka", title="QA", company="Solarwinds", address="Minsk RB",
                            phone_home="80172608247",
                            phone_mobile="80297758679", phone_work="123", fax="123",
                            email_1="1@gmail.com", email_2="2@gmail.com", email_3="3@gmail.com",
                            homepage="https://test", birthday_day="//div[@id='content']/form/select[1]//option[3]",
                            birthday_month="//div[@id='content']/form/select[2]//option[4]",
                            birthday_year="1985",
                            anniversary_day="//div[@id='content']/form/select[3]//option[8]",
                            anniversary_month="//div[@id='content']/form/select[4]//option[3]",
                            anniversary_year="2017",
                            address_2="", phone_home_2="", notes="",
                            group="//div[@id='content']/form/select[5]//option[1]"))
    app.session.logout()
