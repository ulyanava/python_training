# -*- coding: utf-8 -*-

from python_training.model.contact import Contact


def test_test_contact_group(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(first_name="Tania", middle_name="TU", last_name="Ulyanava",
                               nickname="tatianka", title="QA", company="Solarwinds", address="Minsk RB",
                               phone_home="80172608247",
                               phone_mobile="80297758679", phone_work="123", fax="123",
                               email_1="1@gmail.com", email_2="2@gmail.com", email_3="3@gmail.com",
                               homepage="https://test", birthday_day="",
                               birthday_month="",
                               birthday_year="",
                               anniversary_day="",
                               anniversary_month="",
                               anniversary_year="",
                               address_2="", phone_home_2="", notes="",
                               group="//div[@id='content']/form/select[5]//option[1]"))
    app.session.logout()
