# -*- coding: utf-8 -*-

import pytest
from python_training.group import Group
from python_training.application import Application


@pytest.fixture
def app(request):
    # создание объекта типа Application
    fixture = Application()
    # разрушение фикстуры
    request.addfinalizer(fixture.destroy)

    return fixture


def test_add_group2(app):
    app.login(username="admin", password="secret")
    app.create_group_form(Group(name="name", header="header", footer="footer"))
    app.logout()

