# -*- coding: utf-8 -*-

from python_training.model.group import Group


def test_add_group2(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="name", header="header", footer="footer"))
    app.session.logout()
