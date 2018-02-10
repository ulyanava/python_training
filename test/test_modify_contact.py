from python_training.model.contact import Contact


def test_modify_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.modify_first_contact(Contact(first_name="Tania_modified", middle_name="TU_modified",
                                             last_name="Ulyanava_modified",
                                             nickname="tatianka_modified",
                                             title="QA_modified", company="Solarwinds_modified",
                                             address="Minsk RB_modified",
                                             phone_home="80172608247_modified",
                                             phone_mobile="80297758679_modified",
                                             phone_work="123_modified", fax="123_modified",
                                             email_1="1_modified@gmail.com",
                                             email_2="2_modified@gmail.com",
                                             email_3="3_modified@gmail.com",
                                             homepage="https://test_modified",
                                             birthday_day="",
                                             birthday_month="",
                                             birthday_year="",
                                             anniversary_day="",
                                             anniversary_month="",
                                             anniversary_year="",
                                             address_2="_modified", phone_home_2="_modified", notes="_modified",
                                             group="//div[@id='content']/form/select[5]//option[1]"))
    app.session.logout()
